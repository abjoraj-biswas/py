print('''enter the chocie of whioch you want to do the calculation:
1)Addition
2)substraction
3)multiplication
4)division ''')
choice=int(input("enter your choice:"))
a=int(input("enter the 1st nnumber: "))
b=int(input("enter the 2nd number: "))
if choice==1:
    sum=a+b
    print("the sum of ",a,"and",b,"is",sum)
elif choice==2: 
    sub=a-b
    print("the result of subtraction of",a,"and",b,"is",sub)
elif choice==3:
    multi=a*b
    print("the result of multiplication of ",a,"and",b,"is",multi)
else:
   divd=a/b
   print("the result of division of ",a,"and",b,"is",divd)
