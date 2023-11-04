import pandas as pd

file = "format.xlsx"
df = pd.read_excel(file)

normalizeData = df["Price(Tshs)"]/df["Price(Tshs)"].max()
normalizeData.to_excel("normalizedData.xlsx")