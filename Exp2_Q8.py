"8.Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage."
print("Press Enter to use default values")

# ----- Student Details -----
name = input("Enter Name (default = Rohit Sharma): ")
roll = input("Enter Roll Number (default = R17234512): ")
sapid = input("Enter SAPID (default = 50005673): ")
sem = input("Enter Semester (default = 1): ")
course = input("Enter Course (default = B.Tech. CSE AI&ML): ")

name = name or "Rohit Sharma"
roll = roll or "R17234512"
sapid = sapid or "50005673"
sem = sem or "1"
course = course or "B.Tech. CSE AI&ML"

# ----- Marks -----
pds = int(input("Enter PDS marks (default = 70): ") or 70)
python = int(input("Enter Python marks (default = 80): ") or 80)
chem = int(input("Enter Chemistry marks (default = 90): ") or 90)
eng = int(input("Enter English marks (default = 60): ") or 60)
phy = int(input("Enter Physics marks (default = 50): ") or 50)

# ----- Calculations -----
total = pds + python + chem + eng + phy
percentage = total / 5
cgpa = percentage / 10

# ----- Grade Calculation -----
if 0 <= cgpa <= 3.4:
    grade = "F"
elif 3.5 <= cgpa <= 5.0:
    grade = "C+"
elif 5.1 <= cgpa <= 6:
    grade = "B"
elif 6.1 <= cgpa <= 7:
    grade = "B+"
elif 7.1 <= cgpa <= 8:
    grade = "A"
elif 8.1 <= cgpa <= 9:
    grade = "A+"
elif 9.1 <= cgpa <= 10:
    grade = "O (Outstanding)"
else:
    grade = "Invalid CGPA"

# ----- Output -----
print("\n------- Grade Sheet -------")
print("Name:", name)
print("Roll Number:", roll, "\tSAPID:", sapid)
print("Sem:", sem, "\tCourse:", course)

print("\nSubject\t\tMarks")
print("PDS\t\t", pds)
print("Python\t\t", python)
print("Chemistry\t", chem)
print("English\t\t", eng)
print("Physics\t\t", phy)

print("\nPercentage:", percentage, "%")
print("CGPA:", round(cgpa, 2))
print("Grade:", grade)