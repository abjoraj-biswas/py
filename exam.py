def writing():
    with open ('exam.txt','w') as f:
        b=input('Enter the string:')
        f.write(b)
        print('Data enterted successfully!!')
def reading():
    with open('exam.txt','r')as f:
        print(f.read())
reading()