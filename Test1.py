
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def store():
    products = [
        {"name": "Laptop", "price": 800},
        {"name": "Mouse", "price": 40},
        {"name": "Keyboard", "price": 60}
    ]
    return render_template("store.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
