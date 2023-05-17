#Write a Python program to get unique values from a list

list=[10,20,30,40,10,20,30,40,50,60]
l2 =[] 
for i in list:
        if i not in l2:
            l2.append(i)
       
print(l2)            