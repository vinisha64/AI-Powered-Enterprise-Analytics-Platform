from analytics.data_loader import load_data
from analytics.cleaning import clean_data
from analytics.kpi import calculate_kpis
from ai.recommendation_engine import generate_recommendations

df = load_data("data/raw/sales_data.csv")

clean_df, report = clean_data(df)

kpis = calculate_kpis(clean_df)

recommendations = generate_recommendations(kpis)

print("\nAI RECOMMENDATIONS")
print("-" * 40)

for rec in recommendations:
    print(rec)