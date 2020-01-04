#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")
print("<h2 align='center'> Add a new patient </h2>")
form='''
        <form action="register.py" method="POST">
        <table align="center">
        <tr>
        <td> Patient name:</td>
        <td> <input type="text" name="patientname" required /> </td> 

        </tr>
        <tr>
        <td>Address:</td>
       
        <td> <textarea type="text" name="address" required> </textarea></td>
        </tr>

        <tr>
        <td>Contact:</td>
        <td> <input type="number" name="contact" required /> </td> 
        </tr>

        <tr>
        <td>Disease: </td>       
        <td> <textarea type="text" name="disease" required> </textarea></td>
        </tr>

        <tr>
        <td>Gender:</td>
        <td><input type="radio" name="gender" value="male">Male  <input type="radio" name="gender" value="female">Female
        </td>
         </tr>

         <tr>
        <td>Age:</td>
        <td> <input type="number" name="age" required />  </td> 
         </tr>
      
        <tr>
        <td><input type="submit" name="Register" value="Add patient"> </td>
        </tr> 
         </table>
         </form>'''

print(form)

ret=''' <br><br> <a href="admin.py"> back to admin </a>'''
print(ret)
