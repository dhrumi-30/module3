#Write a Python program to map two lists into a dictionary

key = ["java","python","c++"]
values = [10,20,30]

my_dict = {k: v for k,v in zip(key,values) }

print(my_dict)