Import mysql.connector as sqltor
Mycon=sqltor.connect(host="localhost",user="root",passwd="Mypass",database="test")
If mycon.connected():
print('Successfully Connected to MYSQL database'l
