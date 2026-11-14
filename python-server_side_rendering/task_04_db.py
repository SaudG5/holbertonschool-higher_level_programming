#!/usr/bin/python3
"""Flask app that displays products from JSON, CSV or SQLite."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


def read_json(filename):
    """Return the list of products from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def read_csv(filename):
    """Return the list of products from a CSV file."""
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(filename):
    """Return the list of products from a SQLite database."""
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        try:
            data = read_sql('products.db')
        except sqlite3.Error:
            return render_template('product_display.html',
                                   error="Database error")
    else:
        return render_template('product_display.html',
                               error="Wrong source")

    if product_id is not None:
        found = []
        for product in data:
            if str(product['id']) == product_id:
                found.append(product)
        if not found:
            return render_template('product_display.html',
                                   error="Product not found")
        data = found

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
