import mysql.connector as ms
a=ms.connect(host="localhost",user="root",passwd="root")
if a.is_connected():
    print("connection successfull")
cursor=a.cursor()
cursor.execute(f"create database if not exists fox")
cursor.execute("use fox")
cursor.execute("create table if not exists students(name VARCHAR(20),roll_no INT(5))")
name = "vinay"
roll_no = 42
insert_query = "INSERT INTO students (name, roll_no) VALUES (%s, %s)"
cursor.execute(insert_query, (name, roll_no))
cursor.execute("select * from students")
row=cursor.fetchall()
for i in row:
    print(i)
    print("hi")
a.commit()
a.close()

    
