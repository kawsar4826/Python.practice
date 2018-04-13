from random import randrange
def permute(lst):
    n = len(lst)
    for i in range(n - 1):
        pos = randrange(i, n)
        lst[i], lst[pos] = lst[pos], lst[i]

def faulty_permute(lst):
    n = len(lst)
    for i in range(n - 1):
        pos = randrange(0, n)
        lst[i], lst[pos] = lst[pos], lst[i]


def classify(a):
    sum = 100*a[0] + 10*a[1] + a[2]
    if sum == 123: return 0
    elif sum == 132: return 1
    elif sum == 213: return 2
    elif sum == 231: return 3
    elif sum == 312: return 4
    elif sum == 321: return 5
    else: return -1

def report(a):
    print("1,2,3: ", a[0])
    print("1,3,2: ", a[1])
    print("2,1,3: ", a[2])
    print("2,3,1: ", a[3])
    print("3,1,2: ", a[4])
    print("3,2,1: ", a[5])

def run_test(perm, runs):
    original = [1, 2, 3]
    permutation_tally = 6 * [0]
    for i in range(runs):
        working = original[:]
        perm(working)
        permutation_tally[classify(working)] += 1
    report(permutation_tally)

def main():
    runs = 10000
    print("--- Random permute #1 -----")
    run_test(permute, runs)
    print("--- Random permute #2 -----")
    run_test(faulty_permute, runs)

main()
    
    
    
