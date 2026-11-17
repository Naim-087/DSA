Person = {
    "name" :"Carol",
    "address":{
        "city" : "Paris",
        "zip" : "75001"
    }
}

city = Person ["address"] ["city"]

print(city)