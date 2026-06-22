import pandas as pd


def clean_data(df):

    report = {}

    # Original rows
    report["original_rows"] = len(df)

    # Duplicates
    duplicate_count = df.duplicated().sum()
    report["duplicates"] = duplicate_count

    df = df.drop_duplicates()

    # Missing values
    missing_values = df.isnull().sum().sum()
    report["missing_values"] = int(missing_values)

    # Fill numeric columns
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical columns
    categorical_cols = df.select_dtypes(include="object").columns

    for col in categorical_cols:
        df[col] = df[col].fillna("Unknown")

    # Negative Sales
    negative_sales = (df["Sales"] < 0).sum()
    report["negative_sales"] = int(negative_sales)

    report["cleaned_rows"] = len(df)

    return df, report