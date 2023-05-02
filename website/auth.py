from flask import Flask, Blueprint, flash, render_template, request, redirect, url_for
from .views import home

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    un = request.form.get('username')
    pw = request.form.get('password')
    from main import login, cb
    result = login(un, pw)
    
    if result[0]:
        name = result[1]
        acc1=result[2]
        value = cb(acc1)
        # lname=name
        # balance=value
        return redirect(url_for('views.home', lname=name, balance=value))
    return render_template('login.html')

# @auth.route('/logout')
# def logout():
#     return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET','POST'])
def signup():
    from main import createAcc, nonetype
    data=request.form
    if type(data.get('pin')) != nonetype and type(data.get('balance')) != nonetype:
        if (createAcc(data.get('username'), data.get('password'), data.get('fname'), data.get('mname'), data.get('lname'), data.get('pin'), data.get('balance'))):
            return redirect(url_for('views.home', data.get('fname')))
    return render_template('signup.html')