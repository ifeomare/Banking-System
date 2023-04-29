from flask import Flask, Blueprint, render_template
views = Blueprint('views', __name__)

@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/transactions')
def transactions():
    return '<h1>Transactions</h1>'

@views.route('/account-info')
def accountinfo():
    return '<h1>Modify Your Account</h1>'