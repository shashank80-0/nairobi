# Employees mobile number who were present on 22-06-2020 and know python

SELECT contact.phone_num 
FROM contact
INNER JOIN attendance
ON contact.staff_emp_id = attendance.staff_emp_id AND 
attendance.on_date = "2020-06-22" AND attendance.date_status = "P"
INNER JOIN attribute
ON contact.staff_emp_id  = attribute.staff_emp_id
#WHERE attribute.technology_skill_id = "PY"
;


# Skill count of employees who live in Uttar Pradesh

SELECT COUNT(attribute.technology_skill_id)
FROM attribute
INNER JOIN contact
ON attribute.staff_emp_id = contact.staff_emp_id
INNER JOIN address
ON contact.address_city_id = address.city_id
WHERE address.state_name = "Uttar Pradesh";

# Select Employee name with 3rd highest number of skills without where clause

SELECT staff.first_name, attribute.staff_emp_id, COUNT(attribute.technology_skill_id)
FROM staff
INNER JOIN attribute
ON staff.emp_id = attribute.staff_emp_id 
GROUP BY attribute.staff_emp_id
ORDER BY COUNT(attribute.technology_skill_id) DESC, attribute.staff_emp_id ASC
LIMIT 3,1
;


# Names of people who do not have their skills listed

SELECT staff.emp_id,staff.first_name 
from staff
LEFT OUTER JOIN attribute
ON staff.emp_id = attribute.staff_emp_id
WHERE staff.emp_id NOT IN (SELECT attribute.staff_emp_id FROM attribute);



# Skills of employees whose phone number starts with 8

SELECT staff.first_name, attribute.staff_emp_id, attribute.technology_skill_id, technology.skill_name 
FROM attribute
INNER JOIN contact
ON attribute.staff_emp_id = contact.staff_emp_id
INNER JOIN technology 
ON attribute.technology_skill_id = technology.skill_id
INNER JOIN staff
ON staff.emp_id = attribute.staff_emp_id
WHERE contact.phone_num LIKE "8%"
;

# Date on which the attendance was minimum

SELECT attendance.on_date, COUNT(attendance.date_status)
AS employee_attendance 
FROM attendance	
WHERE attendance.date_status = "P"
GROUP BY attendance.on_date
HAVING MIN(employee_attendance)
LIMIT 1
;
