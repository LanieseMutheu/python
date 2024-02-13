class Animal:
    def animals(self):
        print("can breath")

    def monkey(self):
        print("can walk")

    def elephant(self):
        print("can reproduce")

class Human(Animal):
    def mtu(self):
        print("mtu lives on land")

being = Human()

print(being.elephant())
