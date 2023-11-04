import pandas as pd
file = "split_1.xlsx"
df = pd.read_excel(file)

# mean = df["Price(USD)"].mean()
# print(mean)

df["Price(USD)"] = 1500 * df["Price(USD)"]
df.rename(columns={"Price(USD)": "Price(Tshs)"},inplace=True)

# Save it back to Excel
df.to_excel("format.xlsx", index=False)
