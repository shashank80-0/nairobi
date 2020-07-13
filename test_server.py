from flask import Flask, render_template, url_for, request, redirect
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password = "12345",
        port = 3308
        )
mycursor = mydb.cursor()   
mycursor.execute("USE new_db")

app = Flask(__name__)

@app.route('/')
def start_login():
    return render_template('login.html')

@app.route('/success/<username>-<passw>')
def success(username,passw):
    return ("Successfully logged in " + str(username) + str(passw))


@app.route('/', methods =['POST','GET'])
def login():
    if request.method == 'POST':
        employeeId = request.form['user']
        password = request.form['pass']
        #return redirect(url_for('success',username=employeeId, passw=password))
    else:
        employeeId= request.args.get('user')
        password = request.args.get('pass')
        #return redirect(url_for('success',username=employeeId, passw=password))

    if(find(employeeId,password)):
        #return redirect(url_for('success',username=employeeId, passw=password))
        sql = """SELECT first_name from staff WHERE emp_id = '%s'"""
        mycursor.execute(sql,(employeeId))
        val = mycursor.fetchone()
        username = "".join(str(val))
        print(username)
        return redirect(url_for('home',name=username)) 
    else:   
        #return redirect(url_for('success',username=employeeId, passw=password))
        return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

def find(empId,passwd):
    sql = """SELECT * FROM staff WHERE emp_id = %s AND pass = %s"""
    try:
        mycursor.execute(sql,(empId,passwd))
        val = mycursor.fetchall()
        op = "".join([str(elem) for elem in val])
        if(op == ""):            
            return False
        else:
            return True
    except:
        print("Error: unable to to fetch data")
        return False
    
if __name__ == '__main__':
    app.run("127.0.0.5",8080)
