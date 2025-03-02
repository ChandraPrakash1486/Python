class Person:
    def __init__(self,name, age):
        self._name = name #Protected attributes
        self._age = age
    
    #methods to access the protected attributes
    @property
    def n(self):
        return self._name
    
#property decorator allows us to define a method but we can access it like an "attribute" not like a method
    @property
    def a(self):
        return self._age
    
    @n.setter
    def n(self, name):
        self._name = name
     
    @a.setter
    def a(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
        
p1 = Person("John", 30)
print(p1.n) #John, it calls the getter method, remember we can access it like an attribute
print(p1.a) #30

#or
print(p1._name) #John because it is protected not private
print(p1._age) #30

#property decorators also works with private attributes in the same way as it works with protected attributes