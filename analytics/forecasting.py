import pandas as pd


def monthly_sales_forecast(df):

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    monthly_sales = (
        df.groupby(
            df["Order Date"].dt.to_period("M")
        )["Sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["Order Date"] = (
        monthly_sales["Order Date"]
        .astype(str)
    )

    return monthly_sales