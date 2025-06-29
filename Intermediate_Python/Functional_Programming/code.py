from functools import reduce
from functools import partial

#pure functions
def addition(x, y):
    return x + y

print(addition(4,5))

#first class functions/citizens
def Evening():
    return "Evening"
def evening():
    return "Evening"
def night():   
    return "Night"


def greet(func):
    return "Good " + func()

print(greet(Evening))
print(greet(evening))
print(greet(night))

#higher order functions- functions that either take first-class functions as arguments, return them as results, or both.
def greet(fcf):
    return "Good " + Evening()

print(greet(Evening))
    
#Lambda functions
def execute(func, n):
    return func(n) #executes the function with the argument n

print(execute(lambda x: "Yes" if x%2==0 else "No", 2))


#Map, Filter, and Reduce: Functional programming tools
#Map
def square(x):
    return list(map(lambda x: x**2, x))

numbers = [1,2,3]
squared_numbers = square(numbers)
#Filter
def filtering(y):
    # return list(map(lambda y: y%2==0, y)) #[False, True, False]
    return list(filter(lambda y: y%2==0, y)) #[4]

print(filtering(squared_numbers))

#Reduce
def reducing(numbers): 
    return reduce(lambda x, y: x * y, numbers) 

print(reducing(numbers)) 


#List Comprehension
list1 = list(x for x in range(1,11) if x%2==0)
print(list1)


#functoool- partial functions
def originalFunction(x, y): #2 arguments
    return x+y

#making a partial argument
partialFunction = partial(originalFunction, y=5)

print(partialFunction(5))#1 argument

#Immutability- Instead of manipulating the List, create a new one
list2 = [1,2,3,4,5]
list3 = [x*2 for x in list2]
print(list3) #Don't confuse it with the list1

#Recursion
def Greeting(numberOfGuests):
    
    print("Uncle: Say Good Evening to The Guest!")
    
    # worst case to stop recursion
    if numberOfGuests == 0:
       print("\nMe: Good Evening to the imaginary Guest!")
       return 
    elif(numberOfGuests == 1):
        print("Me: Good Evening to the last Guest!")
    else:
        print("Me: Good Evening The real Guest!")
    
    # Call the function with one less guest
    Greeting(numberOfGuests - 1)

# Initial call with 10 guests
Greeting(10)
