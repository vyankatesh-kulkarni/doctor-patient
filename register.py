#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
#print("content-type:text/html\r\n\r\n")
import cgi
formdata = cgi.FieldStorage()
patientname = formdata.getvalue("patientname")
address = formdata.getvalue("address")
contact = formdata.getvalue("contact")
disease = formdata.getvalue("disease")
gender = formdata.getvalue("gender")
age = formdata.getvalue("age")

import pymysql
db= pymysql.connect("localhost","root","","vyankatesh")
cursor=db.cursor()
query="INSERT INTO patient(patientname,address,contact,disease,gender,age) VALUES('{}','{}','{}','{}','{}','{}')".format(patientname,address,contact,disease,gender,age)

try:
    cursor.execute(query)
    db.commit()
    #print("succeessfully added")
    print("Location:http://localhost/cgi-bin/doctor_patient/patients.py\r\n\r\n")
except:
    db.rollback()
    print("error in query")
