import pickle 
def add():
    a=[['arvind',107890181],['jivin',8666600],['kriti',1011001]]
    with open('phonebook.dat','wb')as b:
        pickle.dump(a,b)
def modify():
    a=int(input('Enter the number of arvind:'))
    with open ('phonebook.dat','rb')as b:
        c=pickle.load(b)
        for i in c:
            if i[0].lower()=='arvind':
                i[1]=a
                print('Modified Successfully!!')
                break
        else:
            print('Report Error')
add()
modify()
