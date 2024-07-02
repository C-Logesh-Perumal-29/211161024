from flask import Flask, render_template

app = Flask(__name__)

# Sample product details 
products = [
    {"name": "Men's T-Shirt", "price": 1499.00, "rating": 4.5, "discount": 10, "availability": True},
    {"name": "Women's Watch", "price": 7499.00, "rating": 4.0, "discount": 5, "availability": False},
    {"name": "Smartphone", "price": 34999.00, "rating": 5.0, "discount": 15, "availability": True},
    {"name": "Laptop", "price": 49999.00, "rating": 4.2, "discount": 8, "availability": True},
    {"name": "Wireless Headphones", "price": 9999.00, "rating": 4.7, "discount": 12, "availability": False},
    {"name": "Digital Camera", "price": 64999.00, "rating": 4.9, "discount": 20, "availability": True},
    {"name": "Running Shoes", "price": 4499.00, "rating": 3.8, "discount": 7, "availability": True},
    {"name": "Tablet", "price": 24999.00, "rating": 4.6, "discount": 18, "availability": False},
    {"name": "Backpack", "price": 2999.00, "rating": 4.3, "discount": 9, "availability": True},
    {"name": "Smartwatch", "price": 14999.00, "rating": 4.4, "discount": 11, "availability": True},
    {"name": "Bluetooth Speaker", "price": 3999.00, "rating": 4.2, "discount": 10, "availability": True},
    {"name": "Office Chair", "price": 8999.00, "rating": 4.0, "discount": 8, "availability": True},
    {"name": "Gaming Console", "price": 27999.00, "rating": 4.5, "discount": 15, "availability": False},
    {"name": "External Hard Drive", "price": 5999.00, "rating": 4.3, "discount": 12, "availability": True},
    {"name": "Wireless Mouse", "price": 1499.00, "rating": 4.1, "discount": 6, "availability": True},
    {"name": "Fitness Tracker", "price": 6999.00, "rating": 4.7, "discount": 18, "availability": True},
    {"name": "Cookware Set", "price": 5499.00, "rating": 3.9, "discount": 10, "availability": False},
    {"name": "Portable Blender", "price": 2999.00, "rating": 4.6, "discount": 15, "availability": True},
    {"name": "Travel Backpack", "price": 3999.00, "rating": 4.2, "discount": 7, "availability": True},
    {"name": "Smart LED Bulbs", "price": 1999.00, "rating": 4.4, "discount": 9, "availability": False},
]

@app.route('/')
def display_top_products():
    # Sort products by rating in descending order and select top 10
    top_products = sorted(products, key=lambda x: x['rating'], reverse=True)[:10]
    return render_template('index.html', products=top_products)

if __name__ == '__main__':
    app.run(debug=True)
