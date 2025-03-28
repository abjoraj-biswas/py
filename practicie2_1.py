#q.no30
a=eval(input('enter a list of strings'))
a=list(a)
n=0
for i in a:
    if type(i)== str:
       if len(a)>=7:
          n+=1
    else:
        continue
print('the list is :',a)
print('number of list having length more than 7:',n)

