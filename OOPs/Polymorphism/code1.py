#Polymorphism is quiet confusing. It is a concept where a single method can have different implementations.
#In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
#in Polymorphism we apply the concept of Abstarction and Inheritance. 
#Polymorphism means “many forms” and allows different classes to be treated as instances of the same superclass through a shared interface.


class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"
    
class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"
    
dog = Dog("Doggy")
print(dog.speak())

cat = Cat("Kitty")
print(cat.speak())

#In the above example we have a parent class Animal and two child classes Dog and Cat, which inherit the method speak from the parent class.
#The speak method is defined in the parent class but it is implemented in the child classes.
#The speak method in the parent class is said to be abstract, as it does not have any implementation.
#The child classes provide the implementation for the speak method. This is an example of polymorphism.
#in the above example, we use Method Overriding: The subclass provides its own implementation of The superclass method, speak() in this example.

