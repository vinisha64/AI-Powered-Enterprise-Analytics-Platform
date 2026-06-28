import pandas as pd


def clean_data(df):

    report = {}

    # Original rows
    report["original_rows"] = int(len(df))

    # Remove duplicates
    duplicate_count = int(df.duplicated().sum())
    report["duplicates"] = duplicate_count

    df = df.drop_duplicates()

    # Missing values
    missing_values = int(df.isnull().sum().sum())
    report["missing_values"] = missing_values

    # Fill numeric columns with median
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical columns
    categorical_cols = df.select_dtypes(include="object").columns

    for col in categorical_cols:
        df[col] = df[col].fillna("Unknown")

    # Convert order_date to datetime if present
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(
            df["order_date"],
            errors="coerce"
        )

    # Negative sales
    negative_sales = int((df["sales"] < 0).sum())
    report["negative_sales"] = negative_sales

    # Negative profit
    negative_profit = int((df["profit"] < 0).sum())
    report["negative_profit"] = negative_profit

    # Data Quality Score
    quality_score = round(
        (
            1
            - (duplicate_count + missing_values)
            / max(len(df), 1)
        ) * 100,
        2
    )

    report["quality_score"] = quality_score
    report["cleaned_rows"] = int(len(df))

    return df, report