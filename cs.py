import mysql.connector as con
mycon=con.connect(host='localhost',user='root',password='abjoraj2006',database='abjoraj')
if mycon.is_connected()==True:
    print('connection established successfully!!')
else:
    print('Error!!')
s=mycon.cursor()
s.execute('insert into student  values(1,"Raam",11)')
mycon.commit()


