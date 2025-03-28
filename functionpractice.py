a=int(input("enter the marks for physics :"))
b=int(input("enter the marks for chemistry: "))
c=int(input("enter the marks for maths: "))
d=int(input("enter the marks for cs: "))
e=int(input("enter the marks for english: "))
f=(a+b+c+d+e)/200*100
if f >= 80:
    print("A Grade")
elif f>=70 and f<=79:
    print("B Grade")
elif f>=60 and f<= 69:
    print("C Grade")
elif f>=50 and f<=59:
    print("D Grade")
else:
    print("E Grade")