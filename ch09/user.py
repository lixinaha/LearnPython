# 9-3
print("\n9-3")
class User():
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.loging_times = 0

    def describe(self):
        print(self.first_name.title() + " " + self.last_name.title())

    def greating(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

    def increment_login_times(self):
        self.loging_times +=1

    def reset_loging_times(self):
        self.loging_times = 0

ben = User("Ben", "Jack")
ben.describe()
ben.greating()