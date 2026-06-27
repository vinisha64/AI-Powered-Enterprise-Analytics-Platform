from db_connection import get_connection


def create_sales_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales_data (
            row_id INT,
            order_id VARCHAR(50),
            order_date DATE,
            ship_date DATE,
            ship_mode VARCHAR(50),
            customer_id VARCHAR(50),
            customer_name VARCHAR(100),
            segment VARCHAR(50),
            country VARCHAR(100),
            city VARCHAR(100),
            state VARCHAR(100),
            postal_code INT,
            region VARCHAR(50),
            product_id VARCHAR(50),
            category VARCHAR(50),
            sub_category VARCHAR(50),
            product_name TEXT,
            sales NUMERIC,
            quantity INT,
            discount NUMERIC,
            profit NUMERIC
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ sales_data table created successfully!")


if __name__ == "__main__":
    create_sales_table()