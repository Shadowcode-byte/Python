#6.	Program to count number of unique words in a given sentence using sets.
s = input("Enter sentence (default = this is is a test test): ") or "this is is a test test"

words = s.split()
unique_words = set(words)

print("Unique words count =", len(unique_words))