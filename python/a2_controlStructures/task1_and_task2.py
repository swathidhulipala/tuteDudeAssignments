#task_1

var1=input("\nTask1:\nEnter a number: ")
try:
    if int(var1)%2==0:
        print(var1, " is an even number")
    else:
        print(var1, " is an odd number")
except:
    print("Please enter a number, entered value cannot be read as number")
    
#task_2
_sum=0
for i in range(51):
    _sum=_sum+i
print("\nTask2:\nThe sum of numbers from 1 to 50 is ",_sum)