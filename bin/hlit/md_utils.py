import re

from string import Template
from template import STUDENT_TEMPLATE, INSTRUCTOR_TEMPLATE

BHM_IMPORT = "import ButtonHiddenMessage from '~/content/ButtonHiddenMessage.tsx';\n"
DEFAULT_HEADER_INFO = {'current_step': -1, 'lesson_level': -1, 'lesson_number': -1, 'teacher_view': False, 'total_steps': -1}

def parse_md_header(header):
    header_info = dict(x.replace(' ', '').split(':') for x in header.split('\n') if x != '')
    header_info['current_step'] = int(header_info['current_step'])
    header_info['lesson_level'] = int(header_info['lesson_level'])
    header_info['lesson_number'] = int(header_info['lesson_number'])
    header_info['total_steps'] = int(header_info['total_steps'])
    header_info['teacher_view'] = bool(header_info['teacher_view'])

    return header_info

def parse_and_delete_header(content):
    m = re.search(r'---(.*)---', content, re.DOTALL)
    if not m or not m.group(1):
        return DEFAULT_HEADER_INFO, content

    content = content.replace(m.group(0), '')
    header_info = parse_md_header(m.group(1))

    return header_info, content

def replace_md_headings_with_tsx(content, _):
    # replace #'s with hx's
    matches = re.findall(r'^#.*$', content, re.MULTILINE)
    if len(matches) == 0:
        return content

    for match in matches:
        h_num = match.count('#')
        match_text = match.replace('#', '').strip()
        underline = ' underline' if h_num == 1 else ''
        content = content.replace(match, f'<H{h_num}{underline}>{match_text}</H{h_num}>')

    return content

def get_message_and_bhm_from_bhm(content):
    m = re.search(r'<ButtonHiddenMessage.*message=[\'"{](.*)[\'"}]', content, re.DOTALL)
    if not m or not m.group(1):
        return ''

    return m.group(0), m.group(1)

def replace_ntt_with_accordion(content, _):
    if 'NOTE TO TEACHERS' not in content:
        return content

    content = content.replace(BHM_IMPORT, '')
    bhm, message = get_message_and_bhm_from_bhm(content)
    replace_content = f'''<Accordion headerText="Note to teachers" className="my-4" open={{true}}>
  <p className="mt-0">{message}</p>
</Accordion>
    '''

    content = content.replace(bhm, replace_content)

    return content

def parse_and_delete_heading(content):
    m = re.search(r'^<H\d.*$', content, re.MULTILINE)
    if not m:
        return 'TODO: Delete H\'s below and put up here'

    while m:
        content = content.replace(m.group(0), '')
        m = re.search(r'^<H\d.*$', content, re.MULTILINE)

    return content

def convert_to_tsx_template_instructor(student_content, instructor_content, name_prefix):
    header_info, instructor_content = parse_and_delete_header(instructor_content)
    _, student_content = parse_and_delete_header(student_content)

    step_content = parse_and_delete_heading(instructor_content)
    _ = parse_and_delete_heading(student_content)

    return Template(INSTRUCTOR_TEMPLATE).substitute(
        name=name_prefix,
        current_step=header_info['current_step'],
        lesson_number=header_info['lesson_number'],
        total_steps=header_info['total_steps'],
        student_content=student_content,
        teacher_content=instructor_content,
        step_content=step_content,
    )

def convert_to_tsx_template_student(content, name_prefix):
    header_info, content = parse_and_delete_header(content)

    return Template(STUDENT_TEMPLATE).substitute(
        name=name_prefix,
        current_step=header_info['current_step'],
        lesson_number=header_info['lesson_number'],
        total_steps=header_info['total_steps'],
        content=content
    )

def convert_to_tsx_template(student_file_name, instructor_file_name, name_prefix):
    student_content = ''
    instructor_content = ''

    with open(student_file_name, 'r') as f:
        student_content = f.read()
    with open(instructor_file_name, 'r') as f:
         instructor_content = f.read()

    instructor_content = convert_to_tsx_template_instructor(student_content, instructor_content, name_prefix)
    student_content = convert_to_tsx_template_student(student_content, name_prefix)

    with open(instructor_file_name, 'w') as f:
        f.write(instructor_content)
    with open(student_file_name, 'w') as f:
        f.write(student_content)

def double_quotes(content, prefix):
    return content.replace('\'', '"')

def unused_indent(content, prefix):
    return content.replace('import { Indent } from "~/content/styledComponents.tsx";\n', '')

def add_import_to_file(content, import_text):
    imports = re.findall(r'^import.*', content, re.MULTILINE)
    if import_text in imports:
        return content

    imports.append(import_text)
    imports.sort()

    for i, im in enumerate(imports):
        if 'React' in im:
            temp = imports[0]
            imports[0] = im
            imports[i] = temp

        content = content.replace(im, '')

    for im in reversed(imports):
        content = im + '\n' + content

    return content

def styled_link(content, prefix):
    content = content.replace('import { StyledLink } from "~/content/styledComponents.tsx"\n', '')
    content = content.replace(', StyledLink', '')

    m = re.search(r'<StyledLink.*href=(.*).*>(.*)</StyledLink>', content)
    if not m or not m.group(1) or not m.group(2):
        return content

    while m and m.group(1) and m.group(2):
        href = m.group(1)
        link_content = m.group(2).strip()

        new_link = f'''<ButtonWebsite
            color="{prefix}"
            href={href}
            withIcon={{true}}
        >
          {link_content}
        </ButtonWebsite>'''

        content = content.replace(m.group(0), new_link)
        m = re.search(r'<StyledLink.*href=(.*).*>(.*)</StyledLink>', content)

    content = add_import_to_file(content, 'import { ButtonWebsite } from "~/components/Buttons";')

    return content

def replace_md_lists_with_ul(content, prefix):
    # find groups of lists
    # insert UnorderedList component
    # replace md list with li children
    m = re.search(r'-\s(.*)', content)
    if not m:
        return content

    content = content.replace(m.group(0), f'\n<UnorderedList>\n{m.group(0)}')

    while m:
        content = content.replace(m.group(0), f'<li>{m.group(1).strip()}</li>')
        m = re.search(r'-\s(.*)', content)

    content = add_import_to_file(content, 'import UnorderedList from "~/components/List/Unordered";')

    return content

def replace_inline_style_with_tw(content, prefix):
    m = re.search(r'style={{marginTop: "(.*)"}}', content, re.DOTALL)

    if not m or not m.group(1):
        return content

    # add more of these as necessary
    conversion_table = {'20px': 'mt-5'}
    class_name = ''
    value = m.group(1)

    if value not in conversion_table.keys():
        return content

    class_name = f'className="{conversion_table[value]}"'

    content = content.replace(m.group(0), class_name)

    return content

def add_paragraph_tags(content, prefix):
    # TODO
    # paragraphs = re.findall(r'^[A-Z]', content, re.MULTILINE)
    # print(paragraphs)
    # for p in paragraphs:
        # content = content.replace(p, f'<p>{p.strip()}</p>')

    return content

def hs_vs_ms_cards(content, prefix):
    if prefix == 'ms':
        return content.replace('highSchool={true}', 'highSchool={false}')

    return content

def replace_md_bold(content, prefix):
    m = re.search(r'\s\*\*(.*)\*\*\s', content)

    if not m or not m.group(1):
        return content

    while m and m.group(1):
        content = content.replace(m.group(0), f' <strong>{m.group(1)}</strong> ')
        m = re.search(r'\s\*\*(.*)\*\*\s', content)

    return content

def replace_md_italic(content, prefix):
    m = re.search(r'\s_(.*)_\s', content)

    if not m or not m.group(1):
        return content

    while m and m.group(1):
        content = content.replace(m.group(0), f' <em>{m.group(1)}</em> ')
        m = re.search(r'\s_(.*)_\s', content)

    return content

def remove_whitespace(content, prefix):
    content_lines = content.split('\n')
    content_lines = list(filter(lambda x: x != '', content_lines))

    return '\n'.join(content_lines)

def replace_md_links(content, prefix):
    links = re.findall(r'(\[(.*)\]\((.*)\))', content)
    color = "purple" if prefix == "ms" else "indigo"

    if len(links) == 0:
        return content

    for link in links:
        if 'www.' in link[2]:
            content = content.replace(
                link[0],
                f'''<Button
                    action="secondary"
                    color="{color}"
                    href="{link[2]}"
                    icon="external"
                    title="{link[1]}"
                >
                  {link[1]}
                </ButtonWebsite>'''
            )
            continue

        content = content.replace(
            link[0],
            f'''<Button
                action="secondary"
                color="{color}"
                href="{link[2]}"
                icon="download"
                title="{link[1]}"
            >
              {link[1]}
            </Button>'''
        )

    content = add_import_to_file(content, 'import Button from "~/components/button";')

    return content

def delete_multi_h1(content, prefix):
    m = re.search(r'<StudentCard.*(<H1.*</H1>)', content, re.DOTALL)
    if m and m.group(1):
        sub_content = re.sub(r'<H1.*</H1>', '', m.group(0))
        content = content.replace(m.group(0), sub_content)

    return content


def add_newline_above_ex_d(content, prefix):
    m = re.search(r'export default', content)
    if not m:
        return content

    content = content.replace(m.group(0), f'\n{m.group(0)}')

    return content

def add_appropriate_newlines(content, prefix):
    content_lines = content.split('\n')
    for i, line in enumerate(content_lines[:-1]):
        # newline after imports
        if 'import' in line and 'import' not in content_lines[i+1]:
            content_lines.insert(i+1, '')
            continue
        if '<UnorderedList' in line:
            content_lines.insert(i+1, '')
            continue

    # eof
    return '\n'.join(content_lines)+'\n\n'


