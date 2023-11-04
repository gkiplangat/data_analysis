import pandas as pd
import matplotlib.pyplot as plt

# Define the URL and column headers
url_to_read = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
           "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
           "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Read the data from the URL and set the column headers
df = pd.read_csv(url_to_read, names=headers)

# Replace '?' with NaN in the "price" column
df["price"].replace('?', pd.NA, inplace=True)

# Convert the "price" column to numeric (float) to handle NaN values
df["price"] = pd.to_numeric(df["price"], errors='coerce')

# Define the bins for the "price" column
bins = [0, 10000, 20000, 50000, df['price'].max()]
bin_labels = ['Low', 'Medium', 'High', 'Very High']

# Create a new column 'price-category' to store the bin labels
df['price-category'] = pd.cut(df['price'], bins, labels=bin_labels)

# Plot a histogram to visualize the binned data
plt.figure(figsize=(8, 6))
plt.hist(df['price-category'], bins=len(bin_labels), rwidth=0.8, align='left')
plt.title('Price Category Histogram')
plt.xlabel('Price Category')
plt.ylabel('Frequency')
plt.show()
