import pandas as pd
from database.db_connection import get_connection


def load_data(file_path=None):

    # Load data from PostgreSQL
    if file_path is None:
        conn = get_connection()

        query = "SELECT * FROM sales_data"

        df = pd.read_sql(query, conn)

        conn.close()

        return df

    # Load CSV
    elif file_path.endswith(".csv"):
        try:
            df = pd.read_csv(file_path, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding="latin1")

    # Load Excel
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        raise ValueError("Unsupported file format")

    return df