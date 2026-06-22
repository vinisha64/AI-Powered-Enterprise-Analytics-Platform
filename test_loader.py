from analytics.data_loader import load_data

file_path = "data/raw/sales_data.csv"

df = load_data(file_path)

print("\nDataset Loaded Successfully")
print("-" * 40)

print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())