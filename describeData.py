import pandas as pd

url_to_read = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url_to_read)

# Use df.describe() to get summary statistics
summary_stats = df.describe()
summary_stats.to_csv("dataSummary.csv")
