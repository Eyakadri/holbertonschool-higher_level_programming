from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    with open('products.json', 'r') as file:
        return json.load(file)['products']

def read_csv_data():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    try:
        if source == 'json':
            products = read_json_data()
        elif source == 'csv':
            products = read_csv_data()
        else:
            return render_template('product_display.html', 
                                error="Invalid source. Use 'json' or 'csv'")
        
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
