a=int(input("enter the lower limit of the range:"))
b=int(input("enter the lower limit of the range :"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
