import xlsxwriter

# Create a new workbook and add a worksheet
workbook = xlsxwriter.Workbook("C:\\Users\\sudarshan\\OneDrive\\Documents\\file2.xlsx")
worksheet = workbook.add_worksheet()

# Write data to the worksheet
worksheet.write('A1', 'Column1')
worksheet.write('B1', 'Column2')
data = [(1, 'A'), (2, 'B'), (3, 'C')]

for row_num, row_data in enumerate(data, start=1):
    for col_num, cell_data in enumerate(row_data):
        worksheet.write(row_num, col_num, cell_data)

# Close the workbook
workbook.close()
