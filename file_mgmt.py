import xlrd
import pandas as pd
import os.path
import csv

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

def write_excel(result, filename):
    with open(filename, 'w') as output:
        writer = csv.writer(output)
        for key, value in result.items():
            for item in value:
                writer.writerow([item, key])
        print("result is exported to csv file -", filename)