#!/usr/bin/env python3

import sys
import glob

from md_utils import (
    double_quotes, styled_link, unused_indent,
    replace_inline_style_with_tw, hs_vs_ms_cards,
    replace_md_bold, replace_md_italic, replace_md_links,
    replace_md_lists_with_ul, delete_multi_h1, add_paragraph_tags,
    remove_whitespace, add_appropriate_newlines, add_newline_above_ex_d
)
        
from utils import run_functions_on_file

def get_files(lesson_num, step_num):
    instructor_files = glob.glob(f'./src/pages/*/lesson-{lesson_num}/step-{step_num}/notes.tsx', recursive=True)
    student_files = glob.glob(f'./src/pages/*/lesson-{lesson_num}/step-{step_num}.tsx', recursive=True)

    if len(instructor_files) != 2 or len(student_files) != 2:
        print(instructor_files, student_files, 'Error')
        exit(1)

    return instructor_files, student_files

def main(lesson_num, step_num):
    instructor_files, student_files = get_files(lesson_num, step_num)
    functions = [
            double_quotes, styled_link, unused_indent,
            replace_inline_style_with_tw, hs_vs_ms_cards,
            replace_md_bold, replace_md_italic, replace_md_links,
            replace_md_lists_with_ul, delete_multi_h1, add_paragraph_tags,
            remove_whitespace, add_appropriate_newlines, add_newline_above_ex_d
    ]

    for in_file, st_file in zip(instructor_files, student_files):
        run_functions_on_file(in_file, functions)
        run_functions_on_file(st_file, functions)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('USAGE: hlit_dx.py <lesson#> <step#>')
        exit(1)

    main(sys.argv[1], sys.argv[2])

