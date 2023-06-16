# personDict function to create a dictionary of personal info
def personDict(name,age,occupation):
    personInfo = {
        "name" : name,
        "age" : age,
        "occupation" : occupation
    }
    print("Personal Info dictionary created successfully")
    return personInfo

lukeDict = personDict("Luke Skywalker", 19, "Moisture Farmer")
print(lukeDict)