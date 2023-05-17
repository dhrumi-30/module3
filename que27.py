#Write a Python script to sort (ascending and descending) a dictionary by

value = {
    "mark a" : 67,
    "mark b" :40,
    "mark c" : 50,
    "mark d" : 20,
    "mark e" :35 ,
}
print(value)

sorted_value = dict(sorted(value.items(), key=lambda item: item[1]))
print(sorted_value)

sorted_value_desc = dict(sorted(value.items(), key=lambda item: item[1], reverse=True))
print(sorted_value_desc)