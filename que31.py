#Write a Python program to check multiple keys exists in a dictionary

my_dict = {
    "python":24500,
    "c++":20000,
    "java":30000
}
my_dict_check = ["python","c++","java"]

all_key_exist = True

for key in my_dict_check:
    if key not in my_dict:
        all_key_exist =False
        break
    
if all_key_exist:
    print(".....")
else:
    print("*****")        


    if all_key_exist(my_dict,my_dict_check):
        print("multiple key exists in a dictionary")
    else:
        print("multiple key doesn't exists in a dictionary")   