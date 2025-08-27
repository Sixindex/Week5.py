#Object Oriented Programming

#Question 1
class Book:
    def __init__(self, title, author, year):
        self.title = title #attributes of the class
        self.author = author
        self.year = year

    def get_summary(self):#method to return a summary of the book
        return f"'{self.title}' by {self.author}, published in {self.year}." #formatted string to return the summary

Book1 = Book("the Millionaire Fastlane", "MJ DeMarco", 2011) #creating an instance of the Book class
print(Book1.get_summary()) #Output: 'the Millionaire Fastlane' by MJ DeMarco, published in 2011.

Book2 = Book("Atomic Habits", "James Clear", 2018) #creating another instance of the Book class
print(Book2.get_summary()) #Output: 'Atomic Habits' by James Clear, published in 2018.

#Question 2 
#polymorphism 

class Animals:
    def speak(self): #method to be overridden by subclasses
        raise NotImplementedError("Subclasses must implement this method")
    
class Dog(Animals):
    def speak(self): #overriding the speak method for Dog
        return "Woof!"
    
class Cat(Animals):
    def speak(self): #overriding the speak method for Cat
        return "Meow!"
    
class Cow(Animals):
    def speak(self): #overriding the speak method for Cow
        return "Moo!"
#creating instances of each subclass
dog = Dog()
cat = Cat()
cow = Cow()

#calling the speak method on each instance
print(dog.speak()) #Output: Woof!
print(cat.speak()) #Output: Meow!
print(cow.speak()) #Output: Moo!