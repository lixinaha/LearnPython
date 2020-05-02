
# 7-1
print("7-1")
car = input("what car do you want? ")
print( "let me see if i can fin you a " + car)

# 7-2
print("\n7-2")
count = input("how many to come?")
count = int(count)
if count > 8:
    print("no enough rooms")
else:
    print("OK, let's go")

# 7-3
print("\n7-3")
number = int(input("input a number: "))
if number % 10 == 0:
    print("it's 10s")
else:
    print("it's NOT 10s")

# 7-4
print("\n7-4")
pet = ""
while pet != "quit":
    pet = input("input a pet you want, input 'quit' to finish game: ")
    if pet != "quit":
        print("here is your " + pet)

# 7-5
print("\n7-5")
age = 1
while age > 0:
    age = int (input("input your age: "))
    if age < 3:
        print("it's free for you!")
    elif age >= 3 and age < 12:
        print("you should pay $10")
    elif age >= 12:
        print("you should pay $15")

# 7-6
print("\n7-6")
age = 1
active = True
while active:
    age = int (input("input your age: "))
    if age < 3:
        print("it's free for you!")
    elif age >= 3 and age < 12:
        print("you should pay $10")
    elif age >= 12 and age < 100:
        print("you should pay $15")
    elif age == 100:
        active = False
    elif age > 100 and age < 120:
        continue
    elif age >= 120:
        break

# 7-7
print("\n7-7")
print("infinite loop: while True: ")

# 7-8
print("\n7-8")
todo_orders = ["big", "middle", "small"]
done_orders = []
while todo_orders:
    order = todo_orders.pop()
    print("i have a " + order + " cat")
    done_orders.append(order)
print (todo_orders)
print (done_orders)

# 7-9
print("\n7-9")
todo_orders = ["big", "middle", "small", "big", "big", "tiny"]
print("i have no big cat")
while "big" in todo_orders:
    todo_orders.remove("big")
print(todo_orders)

# 7-10
print("\n7-10")
cities = []
active = True
while active:
    city = input("which city do you want to visit(Q to quit): ")
    if city != "Q":
        cities.append(city)
    else:
        active = False
print("i want to go to these cities: " + str(cities))