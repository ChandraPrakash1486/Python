# #  Explicit Getter and Setter Methods
# Another approach is to define explicit methods to access and modify attributes, such as get_attribute() and set_attribute(value). This is less common in Python because properties are preferred, but it still achieves encapsulation by hiding direct attribute access.
class Person:
    def __init__(self, age):
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")

person = Person(25)
print(person.get_age())  # Output: 25
person.set_age(30)
print(person.get_age())  # Output: 30
# person.set_age(-5)     # Raises ValueError