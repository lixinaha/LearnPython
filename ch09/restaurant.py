
class Restaurant():
    def __init__(self, rname, rtype):
        self.name = rname
        self.type = rtype
        self.number_served = 0

    def describe(self):
        print("name is: " + self.name)
        print("type is: " + self.type)

    def open(self):
        print("this restaurant is opening")

    def set_number(self, number):
        self.number_served = number

    def increment_number(self, increment):
        if (self.number_served + increment > 100):
            print("too many clients...")
        else:
            self.number_served += increment
