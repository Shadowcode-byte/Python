#Input a sentence and print words in separate lines.
s = input("Enter sentence (default = Hello world python): ") or "Hello world python"

words = s.split()

for w in words:
    print(w)