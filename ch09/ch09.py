from restaurant import Restaurant
from user import  User

# 9-1
print("\n9-1")
rest1 = Restaurant("Ben's", "fancy")
rest1.describe()
rest1.open()

# 9-2
print("\n9-2")
rest2 = Restaurant("Mike's", "Tiny")
rest3 = Restaurant("Jack's", "Great")
rest4 = Restaurant("Admin's", "Small")

rest2.describe()
rest3.describe()
rest4.describe()

# 9-4
print("\n9-4")
rest5 = Restaurant("Test", "Big")
print("served number is " + str(rest5.number_served))
rest5.set_number(12)
print("served number is " + str(rest5.number_served))

rest5.increment_number(30)
print("served number is " + str(rest5.number_served))
rest5.increment_number(120)
print("served number is " + str(rest5.number_served))

# 9-5
print("\n9-5")
user = User("Que", "Re")
print("login times: " + str(user.loging_times))
user.increment_login_times()
print("login times: " + str(user.loging_times))
user.increment_login_times()
print("login times: " + str(user.loging_times))
user.reset_loging_times()
print("login times: " + str(user.loging_times))

# 9-6
print("\n9-6")
class IceCreamBar(Restaurant):
    def __init__(self, rname, rtype):
        super().__init__(rname, rtype)
        self.flavors = ["Sweet", "Juicy"]


ice_cream = IceCreamBar("Icy", "Small")
ice_cream.describe()
print(ice_cream.flavors)

# 9-8
print("\n9-8")
class SuperPower():
    def __init__(self):
        self.powers = ["add post", "delete post", "ban user"]

    def ShowPowers(self):
        print("I have some power: " + str(self.powers))

class Admin2(User):
      def __init__(self, first, last):
        super().__init__(first, last)
        self.spower = SuperPower()

ben = Admin2("Jack", "Fuse")
ben.describe()
ben.spower.ShowPowers()        

# 9-9
print("\n9-9")
print("super eCar")

# 9-10
print("\n9-10")
rest = Restaurant("Ben", "Tiny")
rest.describe()

# 9-11
print("\n9-11")
from admin import Admin

my_admin = Admin("Ben", "Jim")
my_admin.describe()

# 9-12
print("\n9-12")
print("use models from many files")

# 9-13
print("\n9-13")
from collections import  OrderedDict
words = OrderedDict()
words["add"] = "add an item"
words["remove"] = "delete an item"
words["pop"] = "get the last item"

for k,v in words.items():
    print(k + ": " + v)

# 9-14
print("\n9-14")
from random import randint
x = randint(1,6)

# 9-15
print("\n9-15")
print("visit Python Module of the Week: http://pymotw.com")
