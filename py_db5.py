#inserting multiple data in table with python

import mysql.connector
#conneting to database and select 
mydatabase = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='pythondb')
#for any operation use cursor object
cur = mydatabase.cursor()
#sql command
sql="INSERT INTO student(name,roll,address) VALUES(%s,%s,%s)"
students = [("Bittu",2,"Delhi"),("Ruby",3,"Delhi")] #tuple for placeholder in VALUES
cur.executemany(sql,students)
#To save changes in database
mydatabase.commit()

