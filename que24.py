#Write a Python program to remove an empty tuple(s) from a list of tuples.
mytup=[(1,2,3,4,5),(6,7,8,9,10),(),(),()]

non_empty_tup=[]

for tup in mytup:
    if tup:
        non_empty_tup.append(tup)
        
print(non_empty_tup)        