"""
Text Clustering: file_mgmt

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

``read_excel`` takes the file path as the input and returns it's json format
``write_excel`` takes the dictionary data and writes it csv file

"""

import xlrd
import pandas as pd
import os.path
import csv
import xlsxwriter

def read_excel(file_path):
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)
    return sheet.col_values(0,1)

def read_excel_with_pandas(file_path):
    data = pd.DataFrame()
    ext = os.path.splitext(file_path)[1]
    if ext == 'csv':
        data = pd.read_csv(file_path, index_col=0)
    elif ext == 'xls' or ext == 'xlsx':
        data = pd.read_excel(file_path, index_col=0)
    return data

# def write_excel(result, filename):
#     with open(filename, 'w') as output:
#         writer = csv.writer(output)
#         for key, value in result.items():
#             for item in value:
#                 writer.writerow([item, key])
#
#     print("result is exported to csv file -", filename)

def write_excel(headers, data_array, filename):
    workbook = xlsxwriter.Workbook(filename)
    for sheet_no in range(len(headers)):
        worksheet = workbook.add_worksheet("sheet"+str(sheet_no+1))
        row = 1
        for i in range(len(headers[sheet_no])):
            worksheet.write(0, i, headers[sheet_no][i])
        for key, value in data_array[sheet_no].items():
            for item in value:
                worksheet.write(row, 0, key)
                worksheet.write(row, 1, item)
                row += 1
    workbook.close()