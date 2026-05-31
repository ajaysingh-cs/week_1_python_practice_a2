import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sql_connection import get_sql_connection
import products_dao
import orders_dao
import uom_dao

backend_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(backend_dir)
templates_path = os.path.join(project_root, 'templates')
ui_path = os.path.join(project_root, 'UI')

app = Flask(
    __name__, 
    static_folder=ui_path, 
    static_url_path='/UI',
    template_folder=templates_path
)

CORS(app, resources={r"/*": {"origins": "*"}})
connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    return jsonify(products_dao.get_all_products(connection))

@app.route('/getUOM', methods=['GET'])
def get_uom():
    return jsonify(uom_dao.get_uoms(connection))

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    return jsonify({'product_id': products_dao.insert_new_product(connection, request_payload)})

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    return jsonify(orders_dao.get_all_orders(connection))

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    return jsonify({'order_id': orders_dao.insert_order(connection, request_payload)})

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return jsonify({'product_id': products_dao.delete_product(connection, request.form['product_id'])})

@app.route('/order')
def order_page():
    return render_template('order.html')

@app.route('/')
def dashboard_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000, debug=True)