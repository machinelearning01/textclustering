import xlrd
import pandas as pd

def read_excel(file_path):
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)
    return sheet.col_values(2)

def read_excel_with_pandas(file_path):
    data = pd.read_excel(file_path, index_col=0)
    return data