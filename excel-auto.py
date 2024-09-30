import openpyxl

# Load an existing workbook
wb = openpyxl.load_workbook('datas.xlsx')

# Select the active sheet
sheet = wb.active

# Write data to cells
sheet['A1'] = "Name"
sheet['B1'] = "Age"
sheet['A2'] = "Alice"
sheet['B2'] = 25

# Save the workbook
wb.save('data_updated.xlsx')

print("Excel file updated!")
