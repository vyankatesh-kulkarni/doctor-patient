#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")
import cgi
formdata=cgi.FieldStorage()
pname=formdata.getvalue('patientname')

import pymysql
db=pymysql.connect('localhost','root','','vyankatesh')
cursor=db.cursor()
query="SELECT * FROM patient WHERE patientname='{}'".format(pname)
cursor.execute(query)
data=cursor.fetchall()
#print(data)
table='''<table border ="2" width='1000'>
          <tr>
              <td>id</td>
              <td>name</td>
              <td>address </td>
              <td>contact</td>
              <td>disease</td> 
              <td>gender</td>
               <td>age</td>
          </tr>
          '''
print(table)
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

ret=''' <br> <a href="admin.py"> back to admin </a>'''
print(ret)
