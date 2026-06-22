import pandas as pd

def calculate_kpis(df):

    kpis = {
        "total_revenue": round(df["Sales"].sum(), 2),
        "total_profit": round(df["Profit"].sum(), 2),
        "total_orders": df["Order ID"].nunique(),
        "total_customers": df["Customer ID"].nunique(),
    }

    top_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    top_customer = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    kpis["top_product"] = top_product.index[0]
    kpis["top_customer"] = top_customer.index[0]

    return kpis