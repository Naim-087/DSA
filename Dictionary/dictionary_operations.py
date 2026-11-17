Car = {
    "brand":"Toyota",
    "model":"Camry",
    "year": 2026,
    "color":"blue"
}

print(Car)
print(Car.items())

#remove a key
Car.pop("year")
print(Car)

#Check key exists
print(" 'model' exists:" , "model" in Car)
print(" 'Color' exists :", "year" in Car)