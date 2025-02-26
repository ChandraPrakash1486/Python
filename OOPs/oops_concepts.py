# Importing necessary modules

# Defining a parent class 'Teachers'
class Teachers:
    def __init__(self, name, age, identity, salary=None):
        """
        Initializes the 'Teachers' class.

        Parameters:
        - name: The name of the teacher.
        - age: The age of the teacher.
        - identity: The identity of the teacher.
        - salary (optional): The salary of the teacher.
        """
        self.name = name
        self.age = age
        self.id = identity
        self.salary = salary

    def intro(self):
        """
        Returns a formatted string with the teacher's information.
        """
        output = f'Name: {self.name}\n'
        output += f'Age: {self.age}\n'
        output += f'ID: {self.id}\n'
        if self.salary is not None:
            output += f'Salary: {self.salary}\n'
        return output

# Defining a child class 'Students' which inherits from 'Teachers'
class Students(Teachers):
    def __init__(self, name, age, identity, graduation_year=None):
        """
        Initializes the 'Students' class.

        Parameters:
        - name: The name of the student.
        - age: The age of the student.
        - identity: The identity of the student.
        - graduation_year (optional): The graduation year of the student.
        """
        super().__init__(name, age, identity)
        self.graduation_year = graduation_year

    def intro(self):
        """
        Returns a formatted string with the student's information.
        """
        output = super().intro()
        if self.graduation_year is not None:
            output += f'Graduation Year: {self.graduation_year}'
        return output

# Creating instances of the 'Students' class
student1 = Students("Chandra Prakah", 18, 17, 2027)
student2 = Students("Hemant Lohumi", 20, 22, 2027)

# Printing the information of the students
print(student1.intro())
print(student2.intro())

# Creating an instance of the 'Teachers' class
teacher1 = Teachers("akshay", 18, 17, 20000)

# Printing the information of the teacher
print(teacher1.intro())

# Defining an abstract class 'vehicle'
from abc import ABC, abstractclassmethod
class vehicle(ABC):
    """
    The 'vehicle' class is an abstract class.
    """
    @abstractclassmethod
    def start(self):
        """
        The 'start' method is an abstract method.
        """
        pass

# Defining child classes 'car' and 'bike' which inherit from 'vehicle'
class car(vehicle):
    """
    The 'car' class is a child class of 'vehicle'.
    """
    def start(self):
        """
        The 'start' method prints a message indicating that the car has started.
        """
        print("The car has started")

class bike(vehicle):
    """
    The 'bike' class is a child class of 'vehicle'.
    """
    def start(self):
        """
        The 'start' method prints a message indicating that the bike has started.
        """
        print("The bike has started")

# Creating instances of the 'car' and 'bike' classes
car1 = car()
bike1 = bike()

# Calling the 'start' method on the instances
car1.start()
bike1.start()

#Polymorphism
#1. Inheritance 2. Duck Typing

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism in action
def animal_speaks(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_speaks(dog))  # Output: Woof!
print(animal_speaks(cat))  # Output: Meow!class Duck:

class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm not a duck but Quack!"

def make_quack(obj):
    """
    This function takes an object and calls its quack method.
    
    Parameters:
    obj: Object with a quack method
    
    Returns:
    The result of calling the quack method of the object
    """
    return obj.quack()

duck = Duck()
person = Person()

print(make_quack(duck))    # Output: Quack!
print(make_quack(person))  # Output: I'm not a duck but Quack!
# The function does not care about the type of the object as long as it has the required method.

#aggregation
class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Aggregation: Person contains an Address object

# Create an Address object
address = Address("123 Main St", "Anytown", "CA", "12345")

# Create a Person object with the Address object
person = Person("John Doe", address)

print(person.name)  # Output: John Doe
print(person.address.street)  # Output: 123 Main St

#composition
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started")

class Car:
    def __init__(self, color, engine):
        self.color = color
        self._engine = engine  # Composition: Car contains an Engine object

    def start_engine(self):
        self._engine.start()

# Create an Engine object
engine = Engine(200)

# Create a Car object with the Engine object
car = Car("Red", engine)

car.start_engine()  # Output: Engine started

#nested classes
#1. static: These are classes that are defined inside another class, but are not tied to any instance of the outer class.
class University:
    class Department:
        def __init__(self, name):
            self.name = name

    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

# Create a University object
university = University("Example University")

# Create a Department object
department = University.Department("Computer Science")

# Add the Department object to the University object
university.add_department(department)

print(university.departments[0].name)  # Output: Computer Science

#2. non-static: These are classes that are defined inside another class and are tied to an instance of the outer class.
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    class Department:
        def __init__(self, university, name):
            self.university = university
            self.name = name

    def add_department(self, department):
        self.departments.append(department)

# Create a University object
university = University("Example University")

# Create a Department object
department = university.Department(university, "Computer Science")

# Add the Department object to the University object
university.add_department(department)

print(university.departments[0].name)  # Output: Computer Science


#1. class methods: These are methods that are defined inside a class and are tied to the class itself.


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def create_person(cls, name):
        return cls(name)

    @classmethod
    def get_count(cls):
        return cls.count

# Create a new person using the class method
person = Person.create_person("John")

# Get the count of people using the class method
count = Person.get_count()

print(person.name)  # Output: John
print(count)  # Output: 1

#2. static methods: These are methods that are defined inside a class and are not tied to any instance of the class.

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Use the static methods
result1 = MathUtils.add(5, 3)
result2 = MathUtils.subtract(10, 4)

print(result1)  # Output: 8
print(result2)  # Output: 6


#Magic Methods: Magic methods, also known as dunder methods (double underscore methods), are special methods in Python that provide functionality to classes. These methods are surrounded by double underscores on both sides of their names, hence the name "magic" or "dunder" methods.

# Commonly Used Magic Methods
# __init__: Constructor method that is called when an object is created.
# __str__: Returns a string representation of an object.
# __repr__: Returns a string representation of an object for debugging.
# __len__: Returns the length of an object.
# __getitem__: Enables accessing items in an object using square brackets.
# __setitem__: Enables setting items in an object using square brackets.
# __delitem__: Enables deleting items in an object using square brackets.
# __iter__: Returns an iterator object for an object.
# __next__: Returns the next item in an iterator.
# __call__: Enables calling an object as a function.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

book = Book("Python for Beginners", "John Doe")

print(str(book))  # Output: Python for Beginners by John Doe
print(len(book))  # Output: 20

#Property Decorators: Property decorators, also known as decorators, are decorators that modify the behavior of a method. Property decorators are used to define properties of a class.
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, value):
        first_name, last_name = value.split()
        self._first_name = first_name
        self._last_name = last_name

person = Person("John", "Doe")
print(person.full_name)  # Output: John Doe
person.full_name = "Jane Smith"
print(person.full_name)  # Output: Jane Smith