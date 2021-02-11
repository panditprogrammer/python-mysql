#updating data in table with python

import mysql.connector
#connecting to database and select
mydatabase = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='pythondb')
#for any operation use cursor object
cur = mydatabase.cursor()
#sql command
sql="UPDATE student SET address = 'Ranchi' WHERE name = 'Ruby'"
cur.execute(sql)
#To save changes in database
mydatabase.commit()



