#!/usr/bin/env python3

import sys

from md_utils import *
from utils import *


def clean_content(lesson_number, step_number, name):
    instructor_file_name = f'./src/pages/{name}-school/lesson-{lesson_number}/step-{step_number}/notes.tsx'
    student_file_name = f'./src/pages/{name}-school/lesson-{lesson_number}/step-{step_number}.tsx'
    name_prefix = 'hs' if name == 'high' else 'ms'

    functions = [replace_ntt_with_accordion, replace_md_headings_with_tsx]

    run_functions_on_file(instructor_file_name, functions)
    run_functions_on_file(student_file_name, functions)

    convert_to_tsx_template(student_file_name, instructor_file_name, name_prefix)



def main(args):
    lesson_number = args[1]
    step_number = args[2]

    # # moving instructor files to appropriate locations
    move_instructor_student_files_to_pages(lesson_number, step_number, 'middle')
    move_instructor_student_files_to_pages(lesson_number, step_number, 'high')

    # clean content
    clean_content(lesson_number, step_number, 'middle')
    clean_content(lesson_number, step_number, 'high')

if __name__ == '__main__':
    main(sys.argv)

