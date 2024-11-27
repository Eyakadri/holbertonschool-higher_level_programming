import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    return render_template('items.html', items=items_list)