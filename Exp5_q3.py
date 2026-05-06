#3.	WAP to input a list of scores for N students in a list data type. 
# Find the score of the runner-up and print the output.
n = int(input("Enter N (default = 5): ") or 5)

scores = list(map(int, (input("Enter scores: ") or "2 3 6 6 5").split()))

scores = list(set(scores))   # remove duplicates
scores.sort()

print("Runner-up score =", scores[-2])