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
l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}


t.append("smith")
print(t)