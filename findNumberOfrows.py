import openpyxl

# Specify the Excel file name
excel_file = "dataOne.xlsx"

# Load the Excel file
workbook = openpyxl.load_workbook(excel_file)

# Choose a specific sheet from the Excel file
# Replace 'Sheet1' with the name of the sheet you want to count rows in
sheet = workbook['retaildata']

# Find the maximum row with data in the chosen sheet
max_row = sheet.max_row

print(f"Number of rows with data in '{excel_file}': {max_row}")

