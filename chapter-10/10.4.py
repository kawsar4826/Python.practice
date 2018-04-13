def binary_search(lst, seek):
    first = 0
    last = len(lst) - 1
    while first <= last:
        mid = first + (last - first + 1)//2
        if lst[mid] == seek:
            return mid
        elif lst[mid] > seek:
            last = mid - 1
        else:
            first = mid + 1
    return None
def show(lst):
    for item in lst:
        print("%4d" % item, end='')
    print()

def draw_arrow(value, n):
    print(("%" + str(n) + "s") % "  * ")
    print(("%" + str(n) + "s") % "  * ")
    print(("%" + str(n) + "s%i") % ("**>", value))

def display(lst, value):
    show(lst)
    position = binary_search(lst, value)
    if position != None:
        position = 4*position + 5;
        draw_arrow(value, position)
    else:
        print("(", value, " not in list)", sep='')
    print()

def main():
    a = [2,5,11,13,44,80,100,110]
    display(a, 13)
    display(a, 2)
    display(a, 7)
    display(a, 100)
    display(a, 110)
main()
