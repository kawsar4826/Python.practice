def random_list():
    from random import randrange
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result

def less_than(m, n):
    return m < n

def greater_than(m, n):
    return m > n

def selection_sort(lst, cmp):
    n = len(lst)
    for i in range(n - 1):
        small = i
        for j in range(i + 1, n):
            if cmp(lst[j], lst[small]):
                small = j
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]

def main():
    original = random_list()
    working = original[:]
    print('Original: ', working)
    selection_sort(working, less_than)
    print('Ascending: ', working)
    working = original[:]
    print('Original: ', working)
    selection_sort(working, greater_than)
    print('Descending:', working)
main()
    
    
            
                
