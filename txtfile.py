import csv
def add():
    with open('boomboom.csv','a',newline='')as boom:
        boom1=csv.writer(boom)
        boom1.writerow(['sl.no.','Name of the product','Product id','colour','price'])
        slno=1
        while True:
            a=input('Enter the name of the product:')
            b=int(input('Enter the product id :'))
            c=input('Enter the colour of the prodcut:')
            d=int(input('Enter the price of the product:'))
            e=[slno,a,b,c,d]
            boom1.writerow(e)
            slno+=1
            f=input('Do you want to enter another data(y/n)')
            if f.lower()=='n':
                break
#add()


def read():
    with open('boomboom.csv')as boom:
        boom1=csv.reader(boom)
        for i in boom1:
            print(i)
read()

def search():
    with open('boomboom.csv')as boom:
        boom1=csv.reader(boom)
        a=int(input('Enter the product id of the Product you want to search:'))
        for i in boom1:
            if i[2]==str(a):
                print(i)
                break

search()
