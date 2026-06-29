from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "iPhone 14 Pro", "price": 129900, "description": "Latest Apple iPhone with Dynamic Island"},
    {"name": "Samsung Galaxy S23", "price": 89999, "description": "Flagship Android phone with amazing camera"},
    {"name": "MacBook Air M2", "price": 114900, "description": "Apple laptop with M2 chip"},
    {"name": "Sony WH-1000XM5", "price": 29990, "description": "Noise cancelling headphones"},
    {"name": "Nike Air Force 1", "price": 7495, "description": "Classic white sneakers"}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)