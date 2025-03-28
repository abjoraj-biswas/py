a=eval(input('enetr a list of integers containing both +(ve) and -(ve) elements :'))
pi=[]
ni=[]
for i in a :
    if i>=0:
        pi.append(i)
    if i<0:
        ni.append(i)
print('The origninal list is =',a)
print('The list of positive integers are =',pi)
print('The list of negetive integers are =',ni)

