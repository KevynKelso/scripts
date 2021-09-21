import glob
import os

def find_instructor_files(lesson_number, step_number, name):
    instructor_screen_files = glob.glob(
            f'**/*{name}*/**/*lesson*{lesson_number}/*nstructor*/*screen_{step_number}[_.]*',
            recursive=True
    )
    if len(instructor_screen_files) != 1:
        print(instructor_screen_files, 'Error')
        exit(1)

    return instructor_screen_files[0]

def find_student_file(lesson_number, step_number, name):
    lesson_file_name = glob.glob(
            f'**/*{name}*/*lesson*{lesson_number}/*udent*/screen_{step_number}[_.]*',
            recursive=True
    )
    if len(lesson_file_name) != 1:
        print(lesson_file_name, "Error")
        exit(1)

    return lesson_file_name[0]

def run_functions_on_file(file_name, functions):
    prefix = 'ms' if 'middle' in file_name else 'hs'

    content = ''
    with open(file_name, 'r') as f:
        content = f.read()

    for func in functions:
        content = func(content, prefix)

    with open(file_name, 'w') as f:
        f.write(content)

def read_delete_create_file(old_file_name, new_file_name):
    content = ''
    with open(old_file_name, 'r') as f:
        content = f.read()

    os.remove(old_file_name)

    os.makedirs(os.path.dirname(new_file_name), exist_ok=True)
    with open(new_file_name, 'w') as f:
        f.write(content)

# high_school, middle_school, both have instuctor and student files
def move_instructor_student_files_to_pages(lesson_number, step_number, name):
    instructor_fn = find_instructor_files(lesson_number, step_number, name)
    new_instructor_fn = f'./src/pages/{name}-school/lesson-{lesson_number}/step-{step_number}/notes.tsx'
    read_delete_create_file(instructor_fn, new_instructor_fn)

    student_fn = find_student_file(lesson_number, step_number, name)
    new_student_fn = f'./src/pages/{name}-school/lesson-{lesson_number}/step-{step_number}.tsx'
    read_delete_create_file(student_fn, new_student_fn)

