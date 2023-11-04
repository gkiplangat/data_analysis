import pandas as pd
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

url_to_read = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url_to_read, names=headers)

# headfiles = df.head(10)

# Write the first 10 rows to a CSV file
# headfiles.to_csv("first_10_rows.csv", index=False)

# print(df.dtypes)
df["price"] = df["price"].astype("float")

