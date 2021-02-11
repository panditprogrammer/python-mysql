#Deleting data in table with python

import mysql.connector
#now selecting database 
mydatabase = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='pythondb')
#for any operation use cursor object
cur = mydatabase.cursor()
#sql command
sql="DELETE FROM student WHERE roll = 2"
cur.execute(sql)
#To save changes in database
mydatabase.commit()


