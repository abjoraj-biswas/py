a=int(input('enter the number :'))
b=a
d=len(str(b))
s=0
while a!=0:
    c=a%10
    s=s+c**d
    a=a//10
if s==b:
    print('The numeber is a armstrong number')
else:
    print('The number is not a armstrong number')