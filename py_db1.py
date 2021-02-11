import mysql.connector
#conneting to database
mydatabase = mysql.connector.connect(host='localhost',user='root',password='')
print(mydatabase.connection_id)#this is for checking connection stablished or not
