#!/usr/bin/python3

class Father:
    def __init__(self, age=50):
        print("I'm Father")
        self.age = age

    def my_age(self):
        print(f"Father age is {self.age}")


class Mother:
    def __init__(self, h=8.92):
        print("I'm Mother")
        self.height = h

    def my_height(self):
        print(f"Mother height is {self.height}")

    def my_age(self):
        print(f"I don't know Mother age - BUT {self.my_height()}")


class Child(Mother, Father):
    def __init__(self, weight, height, age):
        Father.__init__(self, age)
        Mother.__init__(self, height)
        print("I'm Child")
        self.weight = weight

    def my_weight(self):
        print(f"Child weight is {self.weight}")


if __name__ == "__main__":
    # ali = Father()
    lupin = Child(weight=75, height=8.97, age=35)

    lupin.my_age()
    lupin.my_weight()
    lupin.my_height()
