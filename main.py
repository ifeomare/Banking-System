import mysql.connector
from website import create_app, account
from website.account import Account
import random

app = create_app()

# acc1=None
global connection
connection = mysql.connector.connect(user = 'newsier', database = 'banking', password = '#Chocmilkshake19!')
global cursor
cursor = connection.cursor()

nonetype = type(None)#used to determine if something does not exist
def sameun(username):#finds out if this user entered a duplicate usernmae
    cursor.execute(f"SELECT * FROM accinfo WHERE username = '{username}'")
    getall = cursor.fetchone()
    if type(getall) == nonetype:
        return True
    else:
        return False

def login(un, pw):#check
    flag = False
    name=''
    var = (f"SELECT * FROM accinfo WHERE username = '{un}' AND password = '{pw}'")
    cursor.execute(var)
    getall = cursor.fetchone()
    if type(getall) != nonetype:
        global acc1
        acc1 = Account(getall[0], float(getall[1]), getall[2], getall[3], getall[4], getall[5], getall[6], getall[7])
        flag = True 
        name = acc1.getf()
        return flag, name, acc1
    return flag, name

def createAcc(un, pw, fn, mn, ln, pin, bal):#check
    flag = False
    while not flag:
        if (sameun(un)):#is username available?

            accnumber = random.randint(1857000000, 1857999999)
            print(accnumber, bal, un, pw, pin, fn, mn, ln)
            addaccount = (f"INSERT INTO accinfo (accnum, balance, username, password, pin, fname, mi, lname) VALUES ('{accnumber}', '{bal}', '{un}', '{pw}', '{pin}', '{fn}', '{mn}', '{ln}')")
            cursor.execute(addaccount)
            connection.commit()#updates table
            global acc1
            acc1 = Account(accnumber, float(bal), un, pw, pin, fn, mn, ln)
            flag = True
        return flag

# def accInfo(id):
#     cursor.execute(f"SELECT * FROM accountinfo WHERE id = '{id}'")
#     getall = cursor.fetchone()
#     global acc1
#     acc1 = Account(getall[0], getall[1], getall[2], getall[3], getall[4], getall[5], getall[6])
#     return acc1

def deposit(dep):
    from main import acc1
    acc1.deposit(dep)
    bal = (f"UPDATE accinfo SET balance = '{acc1.checkBalance()}' WHERE accnum = '{acc1.getid()}'")
    cursor.execute(bal)
    connection.commit()
    print('Deposit Successful!')

def withdraw(wd):
    flag = False
    from main import acc1
    if(acc1.withdraw(wd)):
        cursor.execute(f"UPDATE accinfo SET balance = '{acc1.checkBalance()}' WHERE accnum = '{acc1.getid()}'")
        connection.commit()
        flag = True
        # return True, acc1.checkBalance()
    return flag, acc1.checkBalance()

def cb(acc1):
    # from main import acc1
    # from main import acc1
    return acc1.checkBalance()


def clo():
    us
    cursor.close()
    connection.close()


clo
if __name__=='__main__':
    app.run(debug=True)