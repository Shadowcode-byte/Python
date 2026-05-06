#1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)
def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]

    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


lst = list(map(int, (input("Enter numbers: ") or "10 5 8 2 20").split()))

mx, mn = find_max_min(lst)
print("Max =", mx)
print("Min =", mn)