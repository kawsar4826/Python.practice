##### if example##
dividend, divisor = eval(input('Please enter two numbers to divide: '))
 # If possible, divide them and report the result
if divisor != 0:
    quotient = dividend/divisor
print(dividend, '/', divisor, "=", quotient)
print('Program finished')


#### nested if  ####
value = eval(input("Please enter an integer value in the range 0...10: "))
if value >=0:
    if value <= 10:# Second check
        print(value, "is in range")
    else:
        print(value, "is too large")
else:
    print(value, "is too small")
print("Done")

