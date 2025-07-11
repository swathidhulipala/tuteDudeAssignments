import math

#task1
print('\nTask1\n')
def factorial(num):
    if num<2:
        return 1
    else:
        return num*factorial(num-1)
try:
    var1=input('Enter a number \n')
    print('Factorial of ',var1,' is ',factorial(int(var1)))
except:
    print('Expecting a number, please check')
print('\nTask2\n')

try:
    var2=input('Enter a number \n')
    print('Number is ',var2)
    print('Squareroot of the Number is ',math.sqrt(int(var2)))
    print('Natural log of the Number is ',math.log(int(var2)))
    print('Sine of the Number is ',math.sin(int(var2)))
except:
    print('Number required to perform the calculations. Please enter number only')