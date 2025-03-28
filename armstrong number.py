a=int(input("enter the number :"))
s=0
p=a
while(a!=0):
    r=a%10
    a=a//10
    s=s+r**3
if s==p:
    print("the number is armstrong")
else:
    print("the number is not armstorng")