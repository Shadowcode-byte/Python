#2.	Find whether the given number is Armstrong number.
num = int(input("Enter a number: "))

temp = num
power = len(str(num))   # number of digits
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")