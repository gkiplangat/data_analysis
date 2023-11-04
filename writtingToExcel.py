import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob"],
    "Role": ["Sales Rep", "Front Desk"],
    "Salary": [70000, 60000]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Specify the file name for the Excel file
excel_file = "output_files/excel/sample_data.xlsx"

# Write the DataFrame to the Excel file
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' has been created.")
