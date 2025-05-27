import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="allan123",
  database="shopee"
)

mycursor = mydb.cursor()

sql = "insert into cliente (nome, login, senha) values (%s, %s, %s);"
valores = ('Maria', 'maria@gmail.com', 'maria123')

mycursor.execute(sql, valores)
mydb.commit()