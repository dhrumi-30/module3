'''Write a Python script to check if a given key already exists in a
dictionary.'''


school ={
    "dhrumi" : 22,
    "sakshi" : 23,
    "muskan" :40,
}
key = "muskan"
if key in school:
    print(f"{key} exists in the dictionary")
else:
    print(f"{key} does not exist in the dictionary")