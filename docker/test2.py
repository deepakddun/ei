import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dzs05",
  password="Password123",
database="dev"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)