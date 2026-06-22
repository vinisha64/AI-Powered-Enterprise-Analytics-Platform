from analytics.data_loader import load_data
from analytics.forecasting import monthly_sales_forecast

df = load_data("data/raw/sales_data.csv")

forecast = monthly_sales_forecast(df)

print("\nMONTHLY SALES\n")
print(forecast.head())