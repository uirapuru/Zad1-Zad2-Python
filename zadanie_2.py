import pandas as pd

data = pd.read_csv('file.csv')

filtered_data = data[(data["variable"] == "Sales, government funding, grants and subsidies") & (data["unit"] == "DOLLARS(millions)")]
values = pd.to_numeric(filtered_data["value"], errors="coerce")

sum = values.sum()
count = len(filtered_data)
average = sum / count if count else 0
median = values.median()

print(f"Average Sales: {average:.2f}")
print(f"Median: {median:.2f}")
print(f"Number of items: {len(values)}")
print(f"Max: {values.max():.2f}")
print(f"Min: {values.min():.2f}")