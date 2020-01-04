#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")

table='''<table border ="2" width='1000'>
          <tr>
              <th><b> id </b></th>
              <th><b> name </b></th>
              <th><b> address </b></th>
              <th><b>contact </b></th>
              <th><b> disease </b></th> 
              <th><b> gender </b></th>
              <th><b> age </b></th>
          </tr>
          '''
          
print(table)

import pymysql
db=pymysql.connect("localhost","root","","vyankatesh")
cursor=db.cursor()
query="SELECT * FROM patient"
cursor.execute(query)
data=cursor.fetchall()
#print(data)
for row in data:
    print("<tr>")
    print("<td> {}</td>".format(row[0]))
    print("<td> {}</td>".format(row[1]))
    print("<td> {}</td>".format(row[2]))
    print("<td> {}</td>".format(row[3]))
    print("<td> {}</td>".format(row[4]))
    print("<td> {}</td>".format(row[5]))
    print("<td> {}</td>".format(row[6]))
    print("</tr>")

end='''
        </table>
'''
print(end)
#ret='''<br><a href="Location:http://localhost/cgi-bin/doctor_patient/admin.py\r\n\r\n"> Return to main menu </a>'''
ret=''' <br> <a href="admin.py"> back to admin </a>'''
print(ret)
