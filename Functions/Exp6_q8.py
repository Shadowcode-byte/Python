#8.	Write a program to check whether all the values in a dictionary are same or not using lambda function
d = {"a": 1, "b": 1, "c": 1}

result = (lambda x: len(set(x.values())) == 1)(d)

if result:
    print("All values are same")
else:
    print("Not same")