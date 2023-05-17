#Write a Python program to check whether a list contains a sub list

my_list=[10,20,30,40,50,60]
my_list1=[10,20,30]

if all(elem in my_list for elem in my_list1):
    print("list is sublist")
else:
    print("list is not sublist")    