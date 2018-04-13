#x1,x2,x3,x4,x5=eval(input("Please enter the five value:"))
#maximum=max(x1,x2,x3,x4,x5)
#minimum=min(x1,x2,x3,x4,x5)
#print("The minimum value is",minimum,"and the maximum value is ",maximum)

i,j,k=eval(input("please enter the value"))
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print(k==i,"j=",j,"k=",k)
