from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    with open('data/products.json', 'r') as file:
        return json.load(file)

def read_csv_data():
    products = []
    with open('data/products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert id to int and price to float
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source', default='json')
    product_id = request.args.get('id', type=int)
    
    error_message = None
    products = []
    
    if source not in ['json', 'csv']:
        error_message = "Wrong source"
    else:
        try:
            # Read data based on source
            if source == 'json':
                products = read_json_data()
            else:
                products = read_csv_data()
            
            # Filter by id if provided
            if product_id is not None:
                products = [p for p in products if p['id'] == product_id]
                if not products:
                    error_message = "Product not found"
                    
        except FileNotFoundError:
            error_message = f"Error: {source.upper()} file not found"
            
    return render_template('product_display.html',
                         products=products,
                         error_message=error_message)
