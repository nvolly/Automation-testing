# Strings formatting in Python
''''name = "Bob"
greeting = f"Hello, {name}".format()
print(greeting)
name = "Rolf"
print(greeting)

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)}
'''


#Getting user input
""""name = input("enter name: ")
print(name)
size_input = int(input("How big is your house(in square feet): "))
print(type(size_input))
squere_feet = int(input("what square feet: "))
squere_meter = squere_feet / 2
print(f"{squere_feet} is squere feet and {squere_meter:.1f} is squere meter")
"""

#Writing our first Python app
"""user_age = input("Enter your age: ")
years = int(user_age)
months = years * 12
print(f"Your age is {years} and your months are {months}")
"""


#List, tuples, sets
""""l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}
s.add("Bob2")
print(s)"""


#Advanced set operations
"""friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

friends_abroad = friends.union(abroad)
print(friends_abroad)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)"""

#Booleans
"""print(5 == 5)
print(5 > 5)
print(10 != 10)
friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
print(friends == abroad)"""

#If statements
""""day_of_week = input("Enter day: ").lower()

print(day_of_week == "monday")
if day_of_week == "monday":
    print(True)"""


""""movies_watched = {"the matrix", "green book", "her"}
user_movie = input("Enter something you ve watched recently")

if user_movie in movies_watched:
    print(f"Ive watched {user_movie}".lower())
else:
    print("I havent watched that yet")
"""
""""
number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
    elif number - user_number in (1. -1):
        print("You were off by one")
    else:
        print("Sorry, it`s wrong")"""


#loops in Python
""""number = 7
user_input = input("Would you like to play? (Y/n): ")

while user_input != "n":
    break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
        break
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, it`s wrong")

    user_input = input("Try again? (Y/n): ")"""

""""friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in range(4):
    print(f"{friend} is my friend.")

f = [0,1,2,3,4]
for i in range(4):
    print(i)
for i in (f):
    print(i)"""

""""grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(int(total / amount))
"""

""""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)"""
""""
user_input = input("Enter your choice: ").lower()
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")"""

""""Print a list of the even numbers in the "numbers" list below.
numbers = [1,4,3,5]
even = [x for x in numbers if x%2 == 0]
print(even)"""

""""numbers = [1,3,5,4]
doubled = [x*x for x in numbers if x % 2 == 0]
print(doubled)"""

""""friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [x for x in friends if x.startswith("S")]
print(id(starts_s), id(friends) )
"""

""""friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20
print(friend_ages)"""

""""friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]"""
""""print(friends[0]["name"])"""

""""student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {student_attendance[student]}")
"""

#Destructuring variables
""""t = 5, 11
x, y = t
print(x, y)"""


""""student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items()))

for student. attendance in student_attendance.items():
    print(t)
   # print(f"{student}: {attendance}")"""

""""people = [("Bob",42,"Mechanic"),("James",24,"Artist"),("Harry",32,"Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
"""
""""person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)

*head, tail = [1,2,3,4,5]
print(head)
print(tail)"""



#Functions in python
""""def hello():
    print("Hello!")

hello()"""

""""def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in seconds program!")
user_age_in_seconds()
print("Goodbye!")"""

""""def print():
    print("Hello world")
print()"""

""""friends = ["Rolf", "Bob"]
def add_friends():
    friends_name = input("Enter your friend name: ")
    friends = friends + [friends_name]
add_friends()"""


""""friends = []
def add_friend():
    friends.append("Rolf")

add_friend()
print(friends)"""


""""def add(x, y):
    result = x + y
    print(result)
add(5,3)"""


""""def say_hello(name, surname):
    print(f"Hello {name} {surname}")

say_hello("Bob", "Marley")"""

""""def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(4,0)"""

""""def add(x=5,y):
    print(x + y)

add(x=5,y=5)"""

""""default_y = 3
def add(x, y=default_y):
    sum = x + y
    print(sum)

add(5)

default_y = 4
add(2)"""


#Functions return

""""def add(x,y):
    return x + y

add(5, 8)
result = add(5,8)
print(result)"""


""""def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return"You fool!"


result = divide(4,0)
print(result)"""


""""def ad(x,y):
    return x + y
print(ad(5,7))

add = lambda x, y: x + y
print(add(4,4))

def diff(y,z):
    return y - z

diff = lambda y, z: y - z"""

""""print(diff(10,1))"""
""""
def double(x):
    return x * 2
sequence = [1,3,5,9]
doubled = [(lambda x: x*2)(x) for x in sequence]
print(doubled)
doubled2 = list(map(double,sequence))
print(doubled2)
"""

""""
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

user_comp = {user[1]: user for user in users}
print(user_comp("Rolf"))

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]
if password_input == password:
    print("Yours details are correct")
else:
    print("Your details are incorect")"""


# Create a dict variable called student

student = {
    "name": "Jose",
    "school": "Computing",
    "grades": (66,77,88)
}

#assume the argument, data is a dict
#modify the grades variable so it accesses the grades key of the data dictionary

""""def avarage_grade(date):
    grades = data["grades"]
    return sum(grades) / len(grades)"""

""""def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum(student['grades'])
        count = count + len(student['grades'])
        
    return total / count"""

#unpacking arguments

""""def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1,3,5))"""

""""def add(x,y):
    return x + y
nums = [3, 5]
print(add(*nums))
"""
""""def add (x,y):
    return x + y
nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))

print(add(**nums))"""
""""
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

def apply(*args, operator):
    """


""""def named(**kwargs):
    print(kwargs)
named(name="Bob", age = 25)"""





""""#oop
student = {"name": "Rolf", "grades": (89,90,93,78,90)}
def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))"""
""""
class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student('marie', 11)
print(student.name)
print(student.grades)"""

""""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return(f"Person {self.name}, {self.age} years old.")

    def __repr__(self):
        return f"Person({self.name}, {self.age}"

bob = Person("Bob", 35)
print(bob)

"""


""""class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        return sum([item['price'] for item in self.items])
        # Add together all item prices in self.items and return the total."""

""""class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

ClassTest.class_method()"""

""""class Magic:
    def __init__(self, number):
        self.number = number
    def __mul__(self, other):
        return Magic(self.number * other.number)
    def __eq__(self, other):
        return self.number == other.numbers

print(Magic(5) * Magic(10) == Magic(15))"""

""""class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method if {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

ClassTest.static_method()

test = ClassTest()
test.instance_method()
ClassTest.instance_method()

ClassTest.class_method()"""

""""
class Book:
    TYPES = ("hardcover", "paperback")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight +200)



book = Book.hardcover("Harry Potter", 1500)
print(book)

book2 = Book.paperback("Ron Wesley", 4000)
print(book2)"""
""""
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + ' - franchise')

        # Return another store, with the same name as the argument's name, plus " - franchise"
    @staticmethod
    def store_details(store):
        return f'{}, total stock price: {}'.format(store.name, int(store.stock_price))
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
"""

""""class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remain = capacity

    def __str__(self):
        return(f"{self.name}....{self.connected_by}")

printer = Printer("HP", "USB", 500)
print(printer)"""

""""class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books."

shelf = BookShelf(300)

class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter", 120)
print(book)"""

#type hinting

from typing import List
""""def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)
"""
""""class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
book = Book("Laur", 11)
print(book)


class Blocks:
    def __init__(self, building: str, number: int):
        self.building = building
        self.number = number
blocks = Blocks(help, 11)"""

""""
from typing import List

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books"""
""""
import sys
from two_sum import Twosum

print(sys.path)"""


#Errors in Python
""""def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    return dividend/divisor

grades = []
average = divide(sum(grades), len(grades))
print(average) """

class TooManyPagesReadError(ValueError):
    pass
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>")

    def read(self,pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages"
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")

python101 = Book("Python 101", 50)

try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)