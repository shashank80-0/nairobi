from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://root:12345@localhost:3308/new_db')
app.config ['SQLALCHEMY_ECHO'] = False
app.config['FLASK_ENV'] = 'development'

db=SQLAlchemy(app)


class designation(db.Model):
    role_id = db.Column(db.String(2),primary_key=True)
    role_name = db.Column(db.String(45),nullable=False,unique=True)
    

class technology(db.Model):
    skill_id = db.Column(db.String(2),primary_key=True,nullable=False)
    skill_name = db.Column(db.String,nullable=False,unique=True)

class address(db.Model):
    city_id = db.Column(db.String(45),primary_key=True,nullable=False)
    city_name = db.Column(db.String(45),nullable=False)
    state_name = db.Column(db.String(45),nullable=False)
    pincode_num = db.Column(db.Integer,nullable=False)


class staff(db.Model):
    emp_id = db.Column(db.String(11), primary_key=True, nullable=False)
    first_name = db.Column(db.String(45),nullable=False)
    last_name = db.Column(db.String(45),nullable=False)
    birth_date = db.Column(db.DateTime,nullable=False)
    passwd = db.Column(db.String(45),nullable=False)
    designation_role_id = db.Column(db.String(2),db.ForeignKey(designation.role_id),nullable=True)
    roleId = db.relationship('designation', backref = db.backref('roleId'), lazy = True, uselist='False')
    

class attendance(db.Model):
    staff_emp_id = db.Column(db.String(11),db.ForeignKey(staff.emp_id), primary_key=True, nullable=True)
    empId = db.relationship('staff',backref=db.backref('empId'),lazy=True)
    on_date = db.Column(db.DateTime,primary_key = True,nullable=False)
    date_status = db.Column(db.String(1),nullable=False)



class attribute(db.Model):
    attributecol = db.Column(db.Integer,primary_key=True,nullable=False)
    staff_emp_id = db.Column(db.String(11),db.ForeignKey(staff.emp_id), nullable=False)
    #empId = db.relationship('staff',backref=db.backref('empId'),lazy=True)
    technology_skill_id = db.Column(db.String(2),db.ForeignKey(technology.skill_id),nullable=False)
    skillId = db.relationship('technology',backref = db.backref('skillId'),lazy=True,uselist=False)


class contact(db.Model):
    staff_emp_id = db.Column(db.String(11),db.ForeignKey(staff.emp_id),primary_key = True, nullable=False)
    #empId = db.relationship('staff', backref = db.backref('empId'), lazy=True,uselist=False)
    phone_num = db.Column(db.String(10),nullable=False,unique=True)
    email_addr = db.Column(db.String(45),nullable=False,unique=True)
    home_addr = db.Column(db.String(99),nullable=False)
    address_city_id = db.Column(db.String(45),db.ForeignKey(address.city_id),nullable=False)    
    cityId = db.relationship('address', backref=db.backref('cityId'), lazy=True,uselist=False)



'''
def __init__ (emp_id,first_name,last_name,birth_date,passwd,designation_role_id):
    self.emp_id=emp_id
    self.first_name=first_name
    self.last_name=last_name
    self.birth_date=birth_date
    self.passwd=passwd
    self.designation_role_id=designation_role_id
'''


db.create_all()
'''
user = staff.query.filter_by(first_name='Creed').first()
print(user.last_name)
print(user.roleId)
print(user.emp_id)
print(user.designation_role_id)
userContact = contact.query.filter_by(staff_emp_id=user.emp_id).first()
#print(userContact.empId)
print(userContact.cityId)
#print(userContact.city_name)
print(userContact.home_addr)
print(userContact.phone_num)
userAtt = attribute.query.filter_by(staff_emp_id = user.emp_id).all()
for att in userAtt:
    tech = technology.query.filter_by(skill_id = att.technology_skill_id).first()
    print(tech.skill_name)
userAttendance = attendance.query.filter_by(staff_emp_id = user.emp_id).all()
for item in userAttendance:
    print (item.on_date)
    print (item.date_status)
'''


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        employeeId = request.form['user']
        password = request.form['pass']
        user = staff.query.filter_by(emp_id = employeeId).first()
        if(user is None):
            error = """User does not exist!"""
            return render_template('login.html', error = error)
        elif(user.passwd != password):
            error = """Incorrect password!"""
            return render_template('login.html',error = error)
        else:
            return redirect(url_for('home', output = user.first_name))
            
        


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
        elif(contact.query.filter_by(email_addr = email).first() is not None):
            error = """Email address is already registered!"""
            return render_template('signup.html',error = error)
        else:
            print(dob)
            one = str(firstName[0].upper())
            two = str(dob[2:4])
            three = str(dob[5:7])
            four = (dob[8:10])
            five = (lastName[0:2].upper())
            eIdFormat = one+two+'-'+three+'-'+four+five
            print(eIdFormat)
            user = staff(emp_id = eIdFormat,
                         first_name = firstName,
                         last_name = lastName,
                         birth_date = dob,
                         passwd = password,
                         designation_role_id = 'UN')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('start_login'))

@app.route('/home/<output>')
def home(output):
    return render_template('home.html',name = output)

if __name__ == '__main__':
    app.run()





