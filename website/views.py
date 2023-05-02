from flask import Flask, Blueprint, render_template, request, redirect, url_for
views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
def home():
    lname = request.args.get('lname')
    balance = request.args.get('balance')
    from main import nonetype, deposit, withdraw
    if type(lname) == nonetype:
        return redirect(url_for('auth.login'))
    # print(cb())
    data = request.form
    d = data.get('deposit')
    w = data.get('withdraw')
    if d and w:
        deposit(float(d))
        withdraw(float(w))
        return render_template('home.html', lname=lname, balance=balance) + '<p>Deposit and Withdraw Successful</p>'
    else:
        if type(d) != nonetype or type(w) != nonetype:
            if d:
                deposit(float(d))
                return render_template('home.html', lname=lname, balance=(float(balance)+float(d))) + '<p>Deposit Successful</p>'
            else:
                result=withdraw(float(w))
                balance = result[1]
                if result[0]:
                    return render_template('home.html', lname=lname, balance=(float(balance))) + '<p>Withdraw Successful</p>'
                return render_template('home.html', lname=lname, balance=balance) + '<p>Withdrawl Unsuccessful</p>'
    return render_template('home.html', lname=lname, balance=balance)

@views.route('/account-info', methods=['GET', 'POST'])
def modify():
    from website.account import Account
    from main import acc1
    if not acc1.getid():
        return redirect(url_for('auth.login'))
    return render_template('modify.html')

# @views.route('/account-info')
# def accountinfo():
#     return '<h1>Modify Your Account</h1>'