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

