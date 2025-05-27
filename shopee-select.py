import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="allan123",
  database="shopee"
)

mycursor = mydb.cursor()

sql = "select * from cliente"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for (id, nome, email, senha) in myresult:
  print(nome)