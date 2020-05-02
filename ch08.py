
# 8-1
print("8-1")
def display_message():
    print("i can learn python function")

display_message()

# 8-2
print("\n8-2")
def fav_book(title):
    print("one of my favorite book is " + title)

fav_book("To Live")

# 8-3
print("\n8-3")
def make_shirt(size, message):
    print("the shirt size is " + str(size))
    print("the shirt message is " + message)

make_shirt(13, "Hello")
make_shirt(size=20, message="World")    

# 8-4
print("\n8-4")
def make_shirt2(size="L", message="I love Python"):
    print("the shirt size is " + size)
    print("the shirt message is " + message)    

make_shirt2()
make_shirt2(size="M")
make_shirt2(size="S", message="Good job")

# 8-5
print("\n8-5")
def describe_city(city, country="China"):
    print(city + " is in " + country)

describe_city("Beijing")
describe_city("NY", "USA")
describe_city("Shanghai")

# 8-6
print("\n8-6")
def city_country(city, country):
    full_name = city + ", " + country
    return full_name

print(city_country("BJ", "China"))
print(city_country("NY", "USA"))
print(city_country("Tokyo", "Japan"))

# 8-7
print("\n8-7")
def make_album(author, album, counts=0):
    if counts != 0:
        ifo = {"author":author, "album": album, "count": counts}
    else:
        ifo = {"author":author, "album": album}
    return ifo

print(make_album("Jack", "Love"))
print(make_album("Jack", "Love", 12))

# 8-8
print("\n8-8")
def make_album2(author, album):
    ifo = {"author":author, "album": album}
    return ifo

active = True
while active:
    author = input("the author is: ")
    if (author == "q"):
        active = False

    album = input("the album is: ")
    if album == "q":
        active = False

    item = make_album2(author, album)
    print(item)

# 8-9
print("\n8-9")
def show_magic(magics):
    for name in magics:
        print(name)

magics = ["Ben", "Jack", "Mike"]
show_magic(magics)

# 8-10
print("\n8-10")
def make_great(magics, great_magics):
    while magics:
        magic = magics.pop()
        great_magics.append("the Great " + magic)

greats = []        
make_great(magics, greats)
show_magic(greats)

# 8-11
print("\n8-11")
magics = ["Ben", "Jack", "Mike"]
greats = []
make_great(magics[:], greats)
show_magic(greats)
show_magic(magics)

# 8-12
print("\n8-12")
def make_sandwize(*foods):
    for food in foods:
        print(" i have " + food)

make_sandwize("banana")
make_sandwize("apple", "orange", "peach")
make_sandwize("meet", "fruit")        

# 8-13
print("\n8-13")
def build_profile(first, last, **others):
    print("Name: " + first.title() + " " + last.title())
    for k,v in others.items():
        print(k +": " + str(v))

build_profile("Ben", "Grace", age= 22, genden = "M", local= "BJ")

# 8-14
print("\n8-14")
def build_car(factory, car_type, **infos):
    car = {}
    car["factory"] = factory
    car["type"] = car_type
    for k,v in infos.items():
        car[k] = v
    return car

car = build_car("Honda", "Monster", color="blue", year=1982)
print(car)

# 8-15
print("\n8-15")
import ch08_printing

ch08_printing.print_model()

# 8-16
from ch08_printing import print_model
print_model()

from ch08_printing import print_model as pm
pm()

import ch08_printing as p
p.print_model()

from ch08_printing import *
print_model()

# 8-17
print("\n8-17")
print("code review all the functions in this chapter")
