import csv

# Sample data
data = [
    ["Name", "Role", "Salary"],
    ["Alice", "Sales Rep", 70000],
    ["Bob", "Front Desk", 60000],
]

# Specify the file name for the CSV file
csv_file = "sample_data.csv"

# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been created.")
