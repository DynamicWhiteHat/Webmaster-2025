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

@app.route('/solar.html')
def solar():
    return render_template('solar.html')

@app.route('/wind.html')
def wind():
    return render_template('wind.html')

@app.route('/hydroelectric.html')
def hydro():
    return render_template('hydroelectric.html')

@app.route('/geothermal.html')
def geothermal():
    return render_template('geothermal.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)