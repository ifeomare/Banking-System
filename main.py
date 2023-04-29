import mysql.connector
from website import create_app, auth

app = create_app()

def us():
    global connection
    connection = mysql.connector.connect(user = 'root', database = 'banking', password = '#vanmilkshak3')
    global cursor
    cursor = connection.cursor()
    return cursor, connection
    
nonetype = type(None)#used to determine if something does not exist
# def sameun(username):#finds out if this user entered a duplicate usernmae
#     cursor.execute(f"SELECT * FROM accountinfo WHERE username = '{username}'")
#     getall = cursor.fetchone()
#     if type(getall) == nonetype:
#         return False
#     else:
#         return True

def login(un, pw):#check
    flag = False
    print(un, pw)
    # print(url_for('auth.login'))
    us()
    var = (f"SELECT id FROM accountinfo WHERE username = '{un}' AND password = '{pw}'")
    cursor.execute(var)
    getall = cursor.fetchone()
    
    if type(getall) != nonetype:
        getid = getall[0]#row number(id)
        print(id)
        flag = True 
    return flag

def clo():
    us
    cursor.close()
    connection.close()


clo
if __name__=='__main__':
    app.run(debug=True)