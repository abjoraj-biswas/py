while True:
    a=int(input('''Welcome to python Calculator 
    please select the operation which you want to do
    1)Addition
    2)Subtraction
    3)multiplication
    4)division
    5)floor division:
    '''))
    b=int(input('enter your 1st number:'))
    c=int(input('enter your 2nd number:'))
    if a==1:
        d=b+c
        print('The sum of the given numbers are :',d)
    elif a==2:
        d=b-c
        print('The diffrence between the two given numbers are:',d)
    elif a==3:
        d=b*c
        print('the product of the given two numbers are',d)
    elif a==4:
        d=b/c
        print('the division result of the given two numbers are ',d)
    else:
        d=b//c
        print('the floor division product of the given two numbers are',d)
    e=input('Do you want to do another calculation?(yes/no):')
    if e=='no':
        break


