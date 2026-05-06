'''3.	Assume a file city.txt with details of 5 cities in given format:
(cityname population(in lakhs) area(in sq KM) ):
Example:
Dehradun 5.78 308.20
Delhi 190 1484
Open file city.txt and read to:
a.	Display details of all cities
b.	Display city names with population more than 10Lakhs
c.	Display sum of areas of all cities
'''
total_area = 0

with open("city.txt", "r") as f:
    for line in f:
        name, pop, area = line.split()
        pop = float(pop)
        area = float(area)

        # a) All details
        print(name, pop, area)

        # b) Population > 10 lakhs
        if pop > 10:
            print("High population city:", name)

        # c) Sum of area
        total_area += area

print("Total Area =", total_area)