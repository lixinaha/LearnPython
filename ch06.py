
# 6-1
print("\n6-1")
person = {"fname":"Kate", "lname":"Breck", "age":18, "city":"NY"}
print(person["fname"])
print(person["lname"])
print(person["age"])
print(person["city"])

# 6-2
print("\n6-2")
numbers = {"admin":23, "Ben":65, "Kate": 88, "Luise":66}
print("admin loves number " + str(numbers["admin"]))
print("Ben loves number " + str(numbers["Ben"]))
print("Kate loves number " + str(numbers["Kate"]))
print("Luise loves number " + str(numbers["Luise"]))

# 6-3
print("\n6-3")
words = {"and": "both are true", "or": "any is true", "print": "print message on screen"}
print("and: " + words["and"])
print("or: " + words["or"])
print("print: " + words["print"])

# 6-4
print("\n6-4")
words = {"and": "both are true", "or": "any is true", "print": "print message on screen"}
for k,v in words.items():
    print(k + ": " + v)
words["if"] = "check condation is true"
for k,v in words.items():
    print(k + ": " + v)

# 6-5
print("\n6-5")
rivers = {"Nile": "Egypt", "Yangzi": "China", "Nillo": "India"}
for k,v in rivers.items():
    print(k + " runs through " + v)
for k in rivers.keys():
    print (k)
for v in rivers.values():
    print(v)

# 6-6
print("\n6-6")
langs = {"admin":"C", "Ben":"python", "Mike":"C#"}
person = ["Ben", "Jack", "Mike", "Dave"]
for name in person:
    if name in langs.keys():
        print("thanks, " + name)
    else:
        print(name + ", tell me your lang?")
       
# 6-7
print("\n6-7")
person1 = {"fname":"Kate", "lname":"Breck", "age":18, "city":"NY"}
person2 = {"fname":"Ben", "lname":"Aflac", "age":18, "city":"DC"}
person3 = {"fname":"Tom", "lname":"Sare", "age":18, "city":"LA"}
people = [person1, person2, person3]
for p in people:
    print(p)
 
# 6-8
print("\n6-8")
catty = {"name": "cat", "owner":"Ben"}
doggy = {"name": "dog", "owner":"Mike"}
birdy = {"name": "bird", "owner":"Kate"}
pets = [catty, doggy, birdy]
for p in pets:
    print("\na new pet:")
    for k,v in p.items():
        print(k + " is " + v)

# 6-9
print("\n6-9")
places = {"Ben":["BJ", "TJ", "SH"], "Mike": ["Tokyo"], "Cassy": ["NY", "Paris"]}
for name,cities in places.items():
    print(name + " loves: ")
    for city in cities:
        print(city)

# 6-10
print("\n6-10")
numbers = {"admin":[23, 33], "Ben":[65], "Kate": [88,99, 100], "Luise":[66]}
for k,v in numbers.items():
    print(k + " loves: ")
    for n in v:
        print(n)

# 6-11
print("\n6-11")
Beijing = {"code": 10, "local": "North", "people": "20M"}
Tianjing = {"code": 22, "local": "North", "people": "10M"}
Shanghai = {"code": 20, "local": "Sorth", "people": "23M"}
cities = {"BJ":Beijing, "TJ": Tianjing, "SH": Shanghai}
for k,v in cities.items():
    print(k+ " infos:")
    for i,j in v.items():
        print(i + ": is " + str(j))

# 6-12
print("\n6-12")
print("practice more on dict...")