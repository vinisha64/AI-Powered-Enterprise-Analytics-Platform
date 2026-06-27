import pandas as pd
from db_connection import get_connection


def load_data():
    print("📂 Reading CSV...")

    df = pd.read_csv(
        "data/raw/sales_data.csv",
        encoding="cp1252"
    )

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Convert dates
    df["order_date"] = pd.to_datetime(df["order_date"]).dt.date
    df["ship_date"] = pd.to_datetime(df["ship_date"]).dt.date

    conn = get_connection()
    cursor = conn.cursor()

    print("🗑 Clearing old data...")
    cursor.execute("DELETE FROM sales_data")

    print("📥 Inserting data into PostgreSQL...")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO sales_data (
                row_id, order_id, order_date, ship_date, ship_mode,
                customer_id, customer_name, segment, country,
                city, state, postal_code, region,
                product_id, category, sub_category,
                product_name, sales, quantity,
                discount, profit
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s
            )
        """, tuple(row))

    conn.commit()

    print(f"\n✅ {len(df)} rows imported successfully!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_data()