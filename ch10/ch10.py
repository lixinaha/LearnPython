import os 

'''
# 10-1
print("10-1")
with open(os.path.join(os.sys.path[0], "learning_python.txt")) as fileobj:
    content = fileobj.read()
print(content)

with open(os.path.join(os.sys.path[0], "learning_python.txt")) as fileobj:
    for line in fileobj.readlines():
        print(line)

with open(os.path.join(os.sys.path[0], "learning_python.txt")) as fileobj:
    lines = fileobj.readlines()
print(lines)

# 10-2
print("\n10-2")
with open(os.path.join(os.sys.path[0], "learning_python.txt")) as fileobj:
    for line in fileobj.readlines():
        line = line.replace("Python", "C")
        print(line)

# 10-3
print("\n10-3")
message = input("input some message: ")
with open(os.path.join(os.sys.path[0], "guest.txt"), "w") as file:
    file.write(message)

# 10-4
print("\n10-4")
active = True
with open(os.path.join(os.sys.path[0], "guest_book.txt"), "w") as file:
    while active:
        name = input("input your name, Q to quit:")
        if (name == "Q"):
            break
        file.write(name + "\n")

# 10-5
print("\n10-4")
active = True
with open(os.path.join(os.sys.path[0], "why_proraming.txt"), "w") as file:
    while active:
        name = input("input why you love programming, Q to quit:")
        if (name == "Q"):
            break
        file.write(name + "\n")

# 10-6
print("\n10-6")
x = input("input number x: ")
y = input("input number y: ")
try:
    z = int(x) + int(y)
except Exception:
    print("bad input")
else:
    print(str(z))

# 10-7
print("\n10-7")
while True:
    x = input("input number x: ")
    y = input("input number y: ")
    if (x == "q" or y == "q"):
        break
    try:
        z = int(x) + int(y)
    except Exception as identifier:
        print("input is not a number, try agian...")
    else:
        print(str(z))

# 10-8
print("\n10-8")
def open_file(file_name):
    try:
        with open(os.path.join(os.sys.path[0], file_name), "r") as file:
            contents = file.read()
    except FileNotFoundError as ex:
        print("file not found: " + str(ex))
    else:
        print(contents)

open_file("cats.txt")
open_file("dog.txt")

# 10-9
print("\n10-9")
def open_file2(file_name):
    try:
        with open(os.path.join(os.sys.path[0], file_name), "r") as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

open_file2("cats.txt")
open_file2("dog.txt")

# 10-10
print("\n10-10")
def count_the_word(text):
    words = text.split()
    count = 0
    for word in words:
        if word.lower() == "the":
            count += 1
    print("the book has word 'the' many times: " + str(count))    

try:
    with open(os.path.join(os.sys.path[0],"Pride and Prejudice.txt"), "r", encoding="utf-8") as book:
        content = book.read()
except FileNotFoundError as identifier:
    pass
else:
    count_the_word(content)
'''
# 10-11
print("\n10-11")
import json
fav_number = [12,33,46,90]
with open(os.path.join(os.sys.path[0],"numbers.txt"), "w") as doc:
    json.dump(fav_number, doc)

with open(os.path.join(os.sys.path[0],"numbers.txt"), "r") as doc:
    content = json.load(doc)
print(content)

# 10-12
print("\n10-12")

# 10-13
print("\n10-13")
