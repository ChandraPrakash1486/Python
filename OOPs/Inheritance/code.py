class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def start(self):
        print("Starting engine")
        
    def stop(self):
        print("Stopping engine")
        
class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color) #super() is used to call the parent class constructor and methods
        self.model = model
        

car1 = Car("BMW", "Black", "X5")
print(car1.name)
print(car1.color)
print(car1.model)
car1.start() #Note that we are calling the parent class method here, as we have not defined the start method in the child class
car1.stop()

# Output:
# BMW
# Black
# X5
# Starting engine
# Stopping engine

#Python supports multiple inheritance. In multiple inheritance, a class can inherit attributes and methods from more than one parent class.