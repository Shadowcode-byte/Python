#5.	Create multiple suitable exceptions for a file handling program. 

class FileEmptyError(Exception):
    pass

try:
    with open("data.txt", "r") as f:
        content = f.read()
        if content == "":
            raise FileEmptyError("File is empty")
        print(content)

except FileNotFoundError:
    print("File not found")

except FileEmptyError as e:
    print(e)