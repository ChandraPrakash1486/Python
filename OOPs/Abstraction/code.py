from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r
    
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
        
    def area(self):
        return self.l * self.w
    
    def perimeter(self):
        return 2 * (self.l + self.w)
    
c = Circle(5)
print(c.area())
print(c.perimeter())

r = Rectangle(5, 6)
print(r.area())
print(r.perimeter())

# Output:
# 78.5
# 31.400000000000002
# 30
# 22

# It is quiet similar to the Polymorphism. The only difference is that we are using abstract class here.