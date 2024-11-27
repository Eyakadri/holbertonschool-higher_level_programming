from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_sql_data():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
        return products
    except sqlite3.Error as e:
        raise Exception(f"Database error: {str(e)}")

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    try:
        if source == 'json':
            products = read_json_data()
        elif source == 'csv':
            products = read_csv_data()
        elif source == 'sql':
            products = read_sql_data()
        else:
            return render_template('product_display.html', 
                                error="Invalid source. Use 'json', 'csv', or 'sql'")
        
        if product_id:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                return render_template('product_display.html', 
                                    error=f"Product with ID {product_id} not found")
        
        return render_template('product_display.html', products=products)
    
    except FileNotFoundError:
        return render_template('product_display.html', 
                            error="Data source file not found")
    except Exception as e:
        return render_template('product_display.html', 
                            error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)