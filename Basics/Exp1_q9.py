#9.Write a program to convert given seconds into hours, minutes and remaining seconds.
sec = int(input("Enter seconds: "))

hours = sec // 3600
sec = sec % 3600
minutes = sec // 60
seconds = sec % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
