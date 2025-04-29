from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'notOurHouse'

@app.route('/')
def default():
    return redirect(url_for('home'))

@app.route('/home.html')
def home():
    return render_template('index.html')

@app.route('/citations.html')
def citations():
    return render_template('citations.html')

@app.route('/sourcing.html')
def sourcing():
    return render_template('sourcing.html')

@app.route('/safety.html')
def safety():
    return render_template('safety.html')

@app.route('/order.html')
def order():
    return render_template('order.html')

@app.route('/order-pizza.html')
def order_pizza():
    return render_template('order-pizza.html')

@app.route('/order-breadsticks.html')
def order_breadsticks():
    return render_template('order-breadsticks.html')

@app.route('/order-salad.html')
def order_salad():
    return render_template('order-salad.html')

@app.route('/order-drinks.html')
def order_drinks():
    return render_template('order-drinks.html')

@app.route('/order-dessert.html')
def order_dessert():
    return render_template('order-dessert.html')

@app.route('/order-bag.html')
def order_bag():
    return render_template('order-bag.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8000)