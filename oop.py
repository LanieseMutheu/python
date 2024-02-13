# Object Oriented Programming


class People:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

person1 = People("Alvaro",19, "Spain")
person2 = People("Yannah", 16, "America")

print(person1.name, person1.age, person1.country)
print(f"Hi, I am {person1.name}, {person1.age} old, from {person1.country}." )



#         self.name = "Laisie"
#         self.age = 16
#         self.country = "Kenya"
#
# People = People()
#
# people.name = "Frank"
#
# print(people.name)
