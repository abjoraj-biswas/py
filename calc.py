while True:
    a=int(input('''WELCOME TO PYHTON CALCULATOR 
    please enter the  option on which you want to do the calculation
    1)Addition
    2)Substraction
    3)Multiplication/raise to the power
    4)Division
    -'''))
    if a==1:
        b=float(input('enter the first number :'))
        c=float(input('enter the second number :'))
        d=b+c
        print('the sum of',b,'and',c,'is',d)
    elif a==2:
        b=float(input('enter the first number :'))
        c=float(input('enter the second number :'))
        d=b-c
        print('the diffrence between',b,'and',c,'is',d)
    elif a==3:
        e=int(input('''which type of multiplication do you wana do:
                    1)normal multiplication
                    2)raise to the power
                    -'''))
        b=float(input('enter the first number :'))
        c=float(input('enter the second number :'))
        if e==1:
            d=b*c
            print('the product of',b,'and',c,'is',d)
        elif e==2:
            d=b**c
            print('the product of',b,'to the power',c,'is',d)
        else:
            print('enter a valid option')
    elif a==4:
        e=int(input('''which type of devision do you want to do
                    1)normal division
                    2)floor division
                    3)modulas
                    -'''))
        b=float(input('enter the first number :'))
        c=float(input('enter the second number :'))
        if e==1:
            d=b/c
            print('division of',b,'and',c,'is',d)
        elif e==2:
            d=b//c
            print('floor division of',b,'and',c,'is',d)
        elif e==3:
            d=b%c
            print('the modulas of',b,'and',c,'is',d)
        else:
            print('enetr a valuid option')
    f=input('Do you want to continue(yes/no): ')
    if f=='no':
        break

            
        


    
