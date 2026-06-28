import pandas as pd


def monthly_sales_forecast(df):

    df["order_date"] = pd.to_datetime(df["order_date"])

    monthly_sales = (
        df.groupby(
            df["order_date"].dt.to_period("M")
        )["sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["order_date"] = (
        monthly_sales["order_date"]
        .astype(str)
    )

    return monthly_sales