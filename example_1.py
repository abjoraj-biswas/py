import csv
def Add_Teacher():
    with open ('Teacher.csv','w')as a :
        b=csv.writer(a)
        b.writerow(['T_id','T_name','Desig'])
        while True:
            T_id=input('Enter the id of the teacher:')
            T_name=input('Enter the name of the teacher:')
            desig=input('Enter the designation of the teacher:')
            b.writerow([T_id,T_name,desig])
            d=input('Do you want to enter another data?(Y/N):')
            if d.lower()=='n':
                break
Add_Teacher()
            
    
