#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")

form='''
        <h2 align="center"> Search patient</h2>
        <form action="search_code.py" method="POST" align="center">
        Enter name of patient:
        <input type="text" name='patientname' ><br><br>
        <input type='submit' name="submit" value="search">

        </form>'''
print(form)
   
