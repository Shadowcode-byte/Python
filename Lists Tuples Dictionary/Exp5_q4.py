'''4.	Create a dictionary of n persons where key is name and value is city. 
a) Display all names             b) Display all city names
c) Display student name and city of all students.  d) Count number of students in each city.
'''
n = int(input("Enter number of persons (default = 3): ") or 3)
d = {}
for i in range(n):
    name = input("Enter name: ") or "Student"
    city = input("Enter city: ") or "City"
    d[name] = city

# a) Names
print("Names:", d.keys())

# b) Cities
print("Cities:", d.values())

# c) Name & City
for k, v in d.items():
    print(k, "->", v)

# d) Count per city
count = {}

for city in d.values():
    count[city] = count.get(city, 0) + 1

print("Students per city:", count)