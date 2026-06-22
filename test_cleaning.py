from analytics.data_loader import load_data
from analytics.cleaning import clean_data

file_path = "data/raw/sales_data.csv"

df = load_data(file_path)

clean_df, report = clean_data(df)

print("\nDATA QUALITY REPORT")
print("-" * 40)

for key, value in report.items():
    print(f"{key}: {value}")