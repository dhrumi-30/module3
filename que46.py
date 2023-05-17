'''#Write a Python function to calculate the factorial of a number (a
nonnegative integer)'''

def factorial():
    
    num= int(input("Enter a number:"))
    factorial=1

    for i in range(1,num+1):
        factorial=factorial*i
        print("the factorial of ",num ,"is",factorial)
            
factorial()            