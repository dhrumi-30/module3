#Write a Python function to check whether a number is perfect or not.

def perfect_num(number):
    
    divisor_sum= 0
    for i in range(1,number):
        if number % i == 0:
            divisor_sum +=i
            
    return number == divisor_sum
num= int(input("enter a number:"))

result = perfect_num(num)
if result:
    print("the number is perfect number:")
else:
    print("the number is not perfect number")    
        