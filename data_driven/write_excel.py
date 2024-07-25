import os

import openpyxl

# file --> workbook --> sheets --> rows --> cells
file = os.path.dirname(os.path.abspath('.')) + '\\files' + "\\test_data.xlsx"
workbook = openpyxl.open(file)
sheet = workbook["Sheet1"]

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(r, c).value = "Welcome"
workbook.save(file)

