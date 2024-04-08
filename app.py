from flask import Flask, send_file
from api import api
import sqlite3
import csv

app = Flask(__name__, template_folder='templates', static_folder='static')
app.register_blueprint(api, url_prefix='/api')

# Reset the database for demo
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS products''')
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')

# Load data from products.csv
with open('products.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO products (name, price) VALUES (?, ?)", (row['name'], row['price']))
conn.commit()
conn.close()

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)