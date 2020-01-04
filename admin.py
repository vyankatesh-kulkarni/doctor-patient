#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")
print("<div style='font-size:25' align='center'> Hello Doctor !! </div>")
print("<div style='font-size:20' align='center'> I can do following operations </div>")
ui= ''' <p>
       <table border='2' width='400' align='center'>
       <tr>
          <td><b> Opertions </b></td >
          <td><b> Links </b></td >
      </tr>
      <tr>
          <td> Add new patient </td >
          <td><a href="form.py"> click here</a> </td >
     </tr>
      <tr>
          <td> Show all patients </td >
          <td> <a href="patients.py"> click here</a> </td >
      </tr>
      <tr>
          <td> Search a patient </td >
          <td> <a href="search.py"> search here </a> </td >
      </tr>
      <tr>
          <td> About us </td >
          <td> <a href="aboutus.py"> click here</a> </td >
      </tr>
     
      

</table>
       </p>
   '''


print(ui)
