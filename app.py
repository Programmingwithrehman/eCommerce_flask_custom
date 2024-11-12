from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/codes')
def codes():
    return render_template('codes.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/single')
def single():
    return render_template('single.html')

@app.route('/mail')
def mail():
    return render_template('mail.html')

if __name__ == '__main__':
    app.run(debug=True)
