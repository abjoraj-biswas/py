a=eval (input('enter a list of integers containing +(ve) and -(ve) elements:'))
pi=[]
ni=[]
for i in a:
    if i>=0:
        pi.append(i)
    else:
        ni.append(i)
print('The original list:',a)
print('The list of +(ve) integers',pi)
print('The list of -(ve) integers',ni)
