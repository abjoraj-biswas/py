print(" WELCOME TO PYHTON CALCULATOR")
while True:
     print('''
     1)addition
     2)subtraction
     3)multiplication
     4)division''')
     a=int(input("enter the option you want to choose :"))
     b=float(input("eneter the 1st number:"))
     c=float(input("enter the 2nd number "))
     if a==1:
        d=b+c
        print('addition of ',b,'and',c,'is',d)
     elif a==2:
        d=b-c
        print('substraction of ',b,'and',c,'is',d)
     elif a==3:
        d=b*c
        print('multiplication of',b,'and',c,'is',d)
     elif a==4:
         d=b/c
         print('division of',b,'and',c,'is',d)
     else:
         print('enter a valid input')
     next_calculation=print('want to do another calculation yes/no')
     e=input()
     if e=='no':
          break

  