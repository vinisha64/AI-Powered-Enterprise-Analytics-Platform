from analytics.data_loader import load_data
from analytics.cleaning import clean_data
from analytics.kpi import calculate_kpis

df = load_data("data/raw/sales_data.csv")

clean_df, report = clean_data(df)

kpis = calculate_kpis(clean_df)

print("\nKPI REPORT")
print("-" * 40)

for key, value in kpis.items():
    print(f"{key}: {value}")