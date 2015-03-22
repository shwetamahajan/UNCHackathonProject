from app import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import dataset

db = dataset.connect('sqlite:///file.db')


table = db['guests']


@app.route('/', methods=['GET'])
def sign_form():
    return render_template('sign_form.html')

@app.route('/guest_book', methods=['GET'])
def guest_book():
    signatures = table.find()
    return render_template('guest_book.html', signatures=signatures)

@app.route('/submit', methods=['POST'])
def submit():
    signature = dict(name=request.form['name'], message=request.form['message'])
    table.insert(signature)
    return redirect(url_for('guest_book'))