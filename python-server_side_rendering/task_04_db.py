from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    products = [
        {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []

    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    elif source == 'sql':
        data = read_sql_data()
        if data is None:
            return render_template('product_display.html', error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            data = [product for product in data if product['id'] == product_id]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product id")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
