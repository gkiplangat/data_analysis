import pandas as pd

url_to_read = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url_to_read)

# Write the entire DataFrame to a CSV file
df.to_csv("all_data.csv", index=False)
