a=int(input('enter a number '))
if a==1:
    print(a,'is a prime number')
elif a>1:
    for i in range (2,a):
        if a%i==0:
            flag=True
            break
    if flag==True:
        print('the number is not prime number')
    else:
        print('the number is prime number ')
