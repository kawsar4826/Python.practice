divident, divisor=eval(input('Please enter two numbers to devide:'))
if divisor != 0:
        q=divident/divisor
        print(divident, "/", divisor, "=",q)
print('program finished')




x=eval(input('Enter an integer value int he range 0 ...9999:'))
if x<0:
	x=0
if x>9999:
    x=9999
print(end='[')
digit = x//1000
print(digit,end="---")
x%=10

digit = x//100
print(digit,end="---")
x%=100

digit = x//10
print(digit,end="---")
x%=10
print(x,end="")
print("]")


	
