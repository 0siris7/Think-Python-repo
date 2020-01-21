import mysql.connector

#cnx = mysql.connector.connect(user='root', password='root',host='localhost',database='mysql')
cnx = mysql.connector.connect(host='127.0.0.1',database='mysql',user='root',password='root')
cnx.close()