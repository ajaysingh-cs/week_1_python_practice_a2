from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders "
                   "(customer_name, total, datetime) "
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price) "
                           "VALUES (%s, %s, %s, %s)")

    if order['order_details']:
        first_item = order['order_details'][0]
        order_details_data = (
            order_id,
            int(first_item['product_id']),
            float(first_item['quantity']),
            float(first_item['total_price'])
        )
        cursor.execute(order_details_query, order_details_data)

    connection.commit()
    cursor.close()
    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM orders"
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt
        })
    cursor.close()
    return response