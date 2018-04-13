def rev(lst):
    return [] if len(lst) == 0 else rev(lst[1:]) + lst[0:1]

x=[1, 2, 3, 4, 5, 6, 7]
print("Original List : ",x)
print("Reversed List",rev(x))
