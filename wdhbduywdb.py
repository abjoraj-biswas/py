a=int(input('Enter the radius of the circle:'))
b=int(input('''enter the choice
            1)For area
            2)for perimeter'''))
if b==1:
    c=(22/7)*a**2
    print('The area of the circle was found to be:',c)
else:
    c=2*(22/7)*a
    print('The perimeter of the circle was found to be:',c)



