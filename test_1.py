x = 4 
def reset():
    global x
    x = 2
    print(x, end='&')
def update():
    x+= 3
    print(x, end='@')
update()
x = 6
reset()
print(x, end='$')
