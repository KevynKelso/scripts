#!/usr/bin/env python3

import sys
import re
import glob
import xlsxwriter


USAGE = 'USAGE: faunaFuncDep.py <file_paths>\nFiles must be .fql files'

def write_data_col(worksheet, row, col, data_array):
    inc = 0
    for element in data_array:
        worksheet.write(row, col, element)
        row += 1
        inc += 1

    return inc

def extract_deps_data(file_content, data_dep_type):
    matches = re.findall(rf'{data_dep_type}\("[A-Za-z_-]+"\)', file_content)

    deps = []
    for match in matches:
        match = re.sub(rf'{data_dep_type}\("', '', match)
        deps.append(re.sub(r'"\)', '', match))

    return list(set(deps))


def main(dir_path):
    files = glob.glob(f'{dir_path}/*.fql')

    workbook = xlsxwriter.Workbook('faunaFuncDeps.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for file_name in files:
        worksheet.write(row, col, file_name)
        col += 1

        with open(file_name, 'r') as f:
            file_content = f.read().strip()

        collections = extract_deps_data(file_content, 'Collection')
        worksheet.write(row, col, 'Collections:')
        num_rows1 = write_data_col(worksheet, row+1, col, collections)
        col +=1

        indexes = extract_deps_data(file_content, 'Index')
        worksheet.write(row, col, 'Indexes:')
        num_rows2 = write_data_col(worksheet, row+1, col, indexes)
        col +=1

        functions = extract_deps_data(file_content, 'Function') 
        worksheet.write(row, col, 'Functions:')
        num_rows3 = write_data_col(worksheet, row+1, col, functions)
        col = 0

        max_rows = max(num_rows1, num_rows2, num_rows3)
        row += (max_rows + 3)

    workbook.close()


if __name__ == '__main__':
    main(sys.argv[1])
