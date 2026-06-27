import psycopg2


def get_connection():
    """
    Creates and returns a PostgreSQL database connection.
    """

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="enterprise_analytics",
        user="postgres",
        password="Vinisha@2005"
    )

    return conn


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Connected to PostgreSQL successfully!")
        conn.close()
    except Exception as e:
        print("❌ Connection failed!")
        print(e)