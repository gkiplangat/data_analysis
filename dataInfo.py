import pandas as pd

url_to_read = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url_to_read)

# Get summary statistics using df.describe()
info_str = df.info()

# Save the summary statistics to a CSV file

