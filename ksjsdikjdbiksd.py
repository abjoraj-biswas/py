str1=input('enetr a string :')
print('the',str1,'in revers order')
length=len(str1)
for a in range(-1,(-length-1),-1):
    print(str1[a],end='')