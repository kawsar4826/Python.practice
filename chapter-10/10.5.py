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

def ordered_linear_search(lst, seek):
    i = 0
    n = len(lst)
    while i < n and lst[i] <= seek:
        if lst[i] == seek:
            return i
        i += 1
    return None

def test_searches(lst):
    from time import clock
    start = clock()
    n = len(lst)
    for i in range(n):
        if ordered_linear_search(lst, i) != i:
            print("error")
    stop = clock()
    print("Linear elapsed time", stop - start)

    start = clock()
    n = len(lst)
    for i in range(n):
        if binary_search(lst, i) != i:
            print("error")
    stop = clock()
    print("Binary elapsed time", stop - start)

def main():
    SIZE = 200
    test_list = list(range(SIZE))
    test_searches(test_list)
main()
    
