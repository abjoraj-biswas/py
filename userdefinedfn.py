g=0
def addi():
    a=int(input('enter 1st number:'))
    b=int(input('enter 2nd number :'))
    d=a+b
    global g
    g+=1
    print('sum of ',a,'and',b,'is',d)
def subs():
    a=int(input('enter 1st number:'))
    b=int(input('enter 2nd number :'))
    d=a-b
    global g
    g+=1
    print('diffrence  between ',a,'and',b,'is',d)
def multi():
    a=int(input('enter 1st number:'))
    b=int(input('enter 2nd number :'))
    d=a*b
    global g
    g+=1
    print('product of ',a,'and',b,'is',d)
def divi():
    a=int(input('enter 1st number:'))
    b=int(input('enter 2nd number :'))
    d=a//b
    global g
    g+=1
    print('division of ',a,'and',b,'is',d)
while True:
    c=int(input('''WELCOME TO PYTHON CALCULATOR 
                PLEASE SELECT THE TYPE OF OPERATION YOU WANT TO DO:
                1)ADDITON
                2)SUBSTRACTION
                3)MULTIPLICATION
                4)DIVISION:'''))
    if c==1:
        addi()
    elif c==2:
        subs()
    elif c==3:
        multi()
    elif c==4:
        divi()
    else:
        print('PLEASE ENTER A VALID INPUT!!!!!')
    e=int(input('DO YOU WANT TO DO ANOTHER CALCULATION?(PRESS 1 FOR YES AND 2 FOR NO):'))
    if e==2:
        break