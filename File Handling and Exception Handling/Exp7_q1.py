'''1.	Add few names, one name in each row, in “name.txt file”. 
a.Count no of names  
b.Count all names starting with vowel   
c.Find longest name
'''
with open("name1.txt", "w") as f:
    f.write("Amit\n")
    f.write("Rohit\n")
    f.write("Ankit\n")
    f.write("Isha\n")
    f.write("Om\n")
with open("name1.txt", "r") as f:
    names = f.readlines()
print("Total names =", len(names))
count = 0
for name in names:
    if name.strip()[0].lower() in "aeiou":
        count += 1
print("Names starting with vowel =", count)

longest = ""

for name in names:
    name = name.strip()
    if len(name) > len(longest):
        longest = name

print("Longest name =", longest)