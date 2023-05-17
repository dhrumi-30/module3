# Write a Python program to print all unique values in a dictionary.

my_dict={
    "group a":80,
    "group b":70,
    "group c":90,
    "group a":80,
    "group b":70
}
unique_values = set(my_dict.values())

print("unique values in the dictionary:")
for value in unique_values:
    print(value)