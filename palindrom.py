a=int(input("enter the number :"))
d=a
b=c=0
while a!=0:
    b=a%2
    c=c*10+b
    a=a//2
print('The binary of ',d,'is',c)