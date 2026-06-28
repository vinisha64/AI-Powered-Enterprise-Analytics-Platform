from db_connection import get_connection


def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def total_sales():
    query = """
        SELECT ROUND(SUM(sales), 2)
        FROM sales_data;
    """

    result = execute_query(query)

    print(f"\n💰 Total Sales: ${result[0][0]}")


if __name__ == "__main__":
    total_sales()