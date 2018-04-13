def locate(lst, seek):
    for i in range(len(lst)):
        if lst[i] == seek:
            return i
    return None

def format(i):
    if i > 9999:
        print("****")
    else:
        print("%4j" % i)

def show(lst):
    for item in lst:
        print("%4d" % item, end='')
    print()

def draw_arrow(value, n):
    print(("%" + str(n) + "s") % "  * ")
    print(("%" + str(n) + "s") % "  * ")
    print(("%" + str(n) + "s%i") % ("**", value))

def display(lst, value):
    show(lst)
    position = locate(lst, value)
    if position != None:
        position = 4*position + 5;
        draw_arrow(value, position)
    else:
        print("(", value, " not in list)", sep='')
    print()

def main():
    a = [  100, 44, 2, 80, 5, 13, 11, 2, 110]
    display(a, 13)
    display(a, 2)
    display(a, 12)
    display(a, 100)
    display(a, 110)
main()
    
