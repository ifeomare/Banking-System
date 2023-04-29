from flask import Flask, Blueprint, flash, render_template, request, redirect, url_for
from .views import home

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    un = request.form.get('username')
    pw = request.form.get('password')
    print(un)
    from main import login
    
    if login(un, pw):
        return redirect(url_for('views.home'))
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET','POST'])
def signup():
    data = request.form
    print(data)
    return render_template('signup.html')