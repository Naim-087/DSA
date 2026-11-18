dict1 = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

dict2 = {
    "D" : 4,
    "E" : 5,
    "F" : 6
}

#Method 1 : update() - modifies  dict1 in place
dict1.update(dict2)

print(dict1)

#Method 2 : unpacking - creates a new dictionary

dict3 = {
    "G" : 1,
    "H" : 2,
    "I" : 3
}

dict4 = {
    "J" : 4,
    "K" : 5,
    "L" : 6
}

merged = {**dict1 , **dict2}

print(merged)


#Method 3 : merge operator

dict1 = {"a": 1, "b": 2}
merged = dict1 | dict2
print(merged)