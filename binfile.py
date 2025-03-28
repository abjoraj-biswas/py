import pickle
def Countrec(author):
    f=0
    with open('Binaryfile.dat','rb')as bin:
        a=pickle.load(bin)
        for i in a:
            if i[2]==author:
                print(i)
                f+=1
    print(author,'came',f,'times')
author=input('Enter the name of the author')
Countrec(author)