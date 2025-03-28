a=int(input("enter the number:"))
b=int(input("enter the number :"))
if b>a:
    a,b=b,a
c=a*b
while(a%b!=0):
    r=a%b
    a=b
    b=r
print("HCF =",b)
lcm=c/2
print("LCM =",lcm)