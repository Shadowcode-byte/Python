n = int(input("Enter number of movies (default = 2): ") or 2)

movies = []

for i in range(n):
    name = input("Movie name: ") or "ABC"
    year = int(input("Year: ") or 2014)
    director = input("Director: ") or "XYZ"
    cost = int(input("Production cost: ") or 100)
    collection = int(input("Collection: ") or 150)

    movies.append({
        "name": name,
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    })

# a) All details
print("\nAll Movies:")
for m in movies:
    print(m)

# b) Before 2015
print("\nMovies before 2015:")
for m in movies:
    if m["year"] < 2015:
        print(m["name"])

# c) Profit movies
print("\nProfitable Movies:")
for m in movies:
    if m["collection"] > m["cost"]:
        print(m["name"])

# d) By director
dname = input("Enter director name (default = XYZ): ") or "XYZ"

print("\nMovies by director:")
for m in movies:
    if m["director"] == dname:
        print(m["name"])