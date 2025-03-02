class Person:
    def __init__(self,name, age):
        self.__name = name #ivate attribute with name mangling
        self.__age = age
        
    #methods to access the private attributes
    def display(self):
        print(self.__name)
        print(self.__age)
        
    def get_name(self):
        return self.__age
        

p = Person("John", 30)
# print(p.name)#Error
print(p._Person__name) #John
#or
p.display() #John
#or
print(p.get_name())
