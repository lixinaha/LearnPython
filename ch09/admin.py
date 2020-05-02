from user import  User

# 9-7
print("\n9-7")
class Admin(User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.power = ["add post", "delete post", "ban user"]

    def show_power(self):
        print("I have some power: " + str(self.power))

ben = Admin("Ben", "Jammin")
ben.describe()
ben.show_power()