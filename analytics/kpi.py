import pandas as pd


def calculate_kpis(df):

    kpis = {
        "total_revenue": float(round(df["sales"].sum(), 2)),
        "total_profit": float(round(df["profit"].sum(), 2)),
        "total_orders": df["order_id"].nunique(),
        "total_customers": df["customer_id"].nunique(),
    }

    top_product = (
        df.groupby("product_name")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    top_customer = (
        df.groupby("customer_name")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    kpis["top_product"] = top_product.index[0]
    kpis["top_customer"] = top_customer.index[0]

    return kpis