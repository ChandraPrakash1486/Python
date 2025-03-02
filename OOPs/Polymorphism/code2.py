#Duck Typing - Duck Typing: If an object has the required method, Python doesn’t care about its type (“If it walks like a duck and talks like a duck, it’s a duck”).
#simplep put, Duck typing is a concept in programming, particularly common in dynamically typed languages like Python, where an object's suitability is determined by whether it has certain methods or properties, not by its specific type or class. The term comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." In practice, this means that if an object has the method we need, we can use it as if it were the type we expect, without worrying about its actual class or inheritance.


# A dog that barks
class Dog:
    def say_hello(self):
        print("Woof woof!")

# A cat that meows
class Cat:
    def say_hello(self):
        print("Meow meow!")

# A duck that quacks
class Duck:
    def say_hello(self):
        print("Quack quack!")
        
# A human that says hello
class Human:
    def say_hello(self):
        print("Hello!")
        
# A function that calls the say_hello method on the object
def call_hello(obj):
    obj.say_hello()
    
# an entity that does not have a say_hello method
class Car:
    def drive(self):
        print("Vroom Vroom!")
    
d = Dog()
c = Cat()
du = Duck()
h = Human()
car = Car()

call_hello(d)
call_hello(c)
call_hello(du)
call_hello(h)
call_hello(car)


# Output:
# Woof woof!
# Meow meow!
# Quack quack!
# Hello!
# Error: 'Car' object has no attribute 'say_hello'
        
# In the above example, we have four classes Dog, Cat, Duck, and Human, which have a method say_hello.
# The function call_hello takes an object as an argument and calls the say_hello method on the object.
# In Duck Typing, the type or class of the object is not important, as long as it has the required method.
# The call_hello function can take any object that has the say_hello method, such as Dog, Cat, Duck, or Human.
# Python doesn’t support method overloading (same method name, different parameters) like Java. Instead, use default or variable-length arguments if needed. Polymorphism shines through overriding and duck typing.