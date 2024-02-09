fruits = ["peaches", "pears", "apples"]
years = [3, "1994", 2.5, 987, "1994"]

print(fruits, years)

fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("peaches")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.pop(-1)
print(fruits)

fruits.sort()
print(fruits)
