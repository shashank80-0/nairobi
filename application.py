from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
app = Flask(__name__)


app.config ['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://shashank_9634107:akonpass@db4free.net:3306/shashank_db')
app.config ['SQLALCHEMY_ECHO'] = False
app.config ['MAIL_SERVER'] = 'smtp.gmail.com'
app.config ['MAIL_PORT'] = 465
app.config ['MAIL_USERNAME'] = 'photosbackupshashank@gmail.com'
app.config ['MAIL_PASSWORD'] = 'sa@90279808'
app.config ['MAIL_USE_TLS'] = False
app.config ['MAIL_USE_SSL'] = True


db=SQLAlchemy(app)


class role(db.Model):
    role_id = db.Column(db.String(5),primary_key=True)
    role_name = db.Column(db.String(45),nullable=False,unique=True)

class employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(99),nullable=False)
    last_name = db.Column(db.String(99),nullable=False)
    birth_date = db.Column(db.DateTime,nullable=False)
    email_addr = db.Column(db.String(99),nullable=False,unique=True)
    passwd = db.Column(db.String(99),nullable=False)    

class designation(db.Model):
    id_designation = db.Column(db.Integer, primary_key=True,autoincrement=True)
    emp_id = db.Column(db.Integer,db.ForeignKey(employee.emp_id), primary_key =True,nullable=False)
    designation_emp_id = db.relationship('employee', backref = db.backref('designation_emp_id'), lazy=False)
    role_id =db.Column(db.String(5),db.ForeignKey(role.role_id), nullable=False)
    designation_role_id = db.relationship('role', backref =db.backref('designation_role_id'), lazy=False)

class technology(db.Model):
    skill_id = db.Column(db.String(5),primary_key=True,nullable=False)
    skill_name = db.Column(db.String(99),nullable=False,unique=True)

class address(db.Model):
    city_id = db.Column(db.Integer,primary_key=True,nullable=False, autoincrement=True)
    city_name = db.Column(db.String(45),nullable=False)
    state_name = db.Column(db.String(45),nullable=False)
    pincode_num = db.Column(db.String(6),nullable=False)

class attendance(db.Model):
    on_date = db.Column(db.DateTime,primary_key = True,nullable=False)
    emp_id = db.Column(db.Integer,db.ForeignKey(employee.emp_id), primary_key=True, nullable=True)
    attendance_emp_id = db.relationship('employee',backref=db.backref('attendance_emp_id'),lazy=False)
    date_status = db.Column(db.String(1),nullable=False)

class attribute(db.Model):
    emp_id = db.Column(db.Integer,db.ForeignKey(employee.emp_id),primary_key=True, nullable=False)
    attribute_emp_id = db.relationship('employee',backref=db.backref('attribute_emp_id'),lazy=False)
    skill_id = db.Column(db.String(5),db.ForeignKey(technology.skill_id),primary_key=True,nullable=False)
    attribute_skill_id = db.relationship('technology',backref = db.backref('attribute_skill_id'),lazy=False)
    skill_level = db.Column(db.Integer,nullable=False)

class contact(db.Model):
    emp_id = db.Column(db.Integer,db.ForeignKey(employee.emp_id),primary_key = True, nullable=False)
    contact_emp_id = db.relationship('employee', backref = db.backref('contact_emp_id'), lazy=False,uselist=False)
    phone_num = db.Column(db.String(10),nullable=False,unique=True)    
    home_addr = db.Column(db.String,nullable=False)
    city_id = db.Column(db.Integer,db.ForeignKey(address.city_id),nullable=False)    
    contact_city_id = db.relationship('address', backref=db.backref('contact_city_id'), lazy=False,uselist=False)
    profile_ref = db.Column(db.String(1000), nullable=True)

db.create_all()


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        employeeId = request.form['user']
        password = request.form['pass']
        user = employee.query.filter_by(emp_id = employeeId).first()
        if(user is None):
            error = """User does not exist!"""
            return render_template('login.html', error = error)
        elif(user.passwd != password):
            error = """Incorrect password!"""
            return render_template('login.html',error = error)
        else:
            return redirect(url_for('profile', employeeId=employeeId))
            
        


@app.route('/signup',methods = ['POST','GET'])
def signup():
    error = None
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        firstName = request.form['firstname']
        lastName = request.form['lastname']
        phoneNum = request.form['phone']
        dob = request.form['dateofbirth']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirmpassword']
        if(firstName == '' or lastName =='' or phoneNum =='' or
           dob == '' or email == '' or password == '' or cpassword == ''):
            error = """One or more fields are empty!"""
            return render_template('signup.html', error = error)
        elif(password != cpassword):
            error = """Passwords do not match!"""
            return render_template('signup.html',error = error)
        elif(contact.query.filter_by(phone_num = phoneNum).first() is not None):
            error = """Phone number is already registered!"""
            return render_template('signup.html',error = error)
        elif(employee.query.filter_by(email_addr = email).first() is not None):
            error = """Email address is already registered!"""
            return render_template('signup.html',error = error)
        else:
            user = employee(
                         first_name = firstName,
                         last_name = lastName,
                         birth_date = dob,
                         email_addr = email,
                         passwd = password
                         )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))

@app.route('/home/<output>')
def home(output):
    return render_template('home.html',name = output)

@app.route('/forget', methods=['POST','GET'])
def forget():
    error = None
    if request.method == 'GET': 
        return render_template('forget.html')
    elif request.method == 'POST':
        email = request.form['email']
        if(email == ''):
            error = """Email address cannot be empty!"""
            return render_template('forget.html', error = error)
        elif(employee.query.filter_by(email_addr=email).first() is None):
            error = """Email address is incorrect or does not exist!"""
            return render_template('forget.html', error=error)
        else:
            mail = Mail(app)
            msg = Message('Password reset', sender = 'photosbackup@gmail.com', recipients = [email])
            msg.body = """Please follow this link to reset your password!
                            http://localhost:5000/reset
                            Thank you!"""
            mail.send(msg)
            error = """Reset password link has been sent by email!"""
            return (render_template('forget.html', error = error))

@app.route('/reset', methods=['POST','GET'])
def reset():
    error = None
    if request.method == 'GET':
        return render_template('reset.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        confirmPassword = request.form['confirmPass']
        if(email == '' or password == '' or confirmPassword == ''):
            error = """One or more fields are empty!"""
            return render_template('reset.html',error = error)
        elif(password != confirmPassword):
            error = """Passwords do not match!"""
            return render_template('reset.html',error = error)
        elif(employee.query.filter_by(email_addr=email).first() is None):
            error = """Email address is incorrect or does not exist!"""
            return render_template('reset.html', error=error)
        else:
            user = employee.query.filter_by(email_addr = email).first()
            user.passwd = password
            db.session.commit()
            error = """Password has been successfully changed!"""
            return render_template('reset.html',error = error)
            
@app.route('/profile/<employeeId>')
def profile(employeeId):
    user = employee.query.filter_by(emp_id = employeeId).first()
    name = user.first_name + " " + user.last_name
    email = user.email_addr
    user_contact = contact.query.filter_by(emp_id = employeeId).first()
    profile_ref = user_contact.profile_ref
    phone = user_contact.phone_num
    user_address = address.query.filter_by(city_id = user_contact.city_id).first()
    addr = user_address.city_name + ", " + user_address.state_name
    user_designation = designation.query.filter_by(emp_id = employeeId).all()
    desig = ""
    for roles in user_designation:
        temp = role.query.filter_by(role_id=roles.role_id).first()
        desig = desig + temp.role_name + ", "
        print (desig)
    desig = desig[0:len(desig)-2]
    return render_template('profile.html', profile=profile_ref,name=name, role=desig, address=addr, email = email, phone=phone)
        
    

if __name__ == '__main__':
    app.run()



