a=input('enter the stirng:')
b=len(a)
c=0
d=1
while c!=b:
    if c==b-1:
        print(a[c:d],end='')
    else:
        print(a[c:d],end='-')
    c+=1
    d+=1