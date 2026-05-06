#7.	Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.
tasks = []

while True:
    print("\n1.Add 2.View 3.Remove 4.Exit")
    ch = input("Enter choice: ") or "4"

    if ch == "1":
        tasks.append(input("Enter task: "))

    elif ch == "2":
        print("Tasks:", tasks)

    elif ch == "3":
        t = input("Enter task to remove: ")
        if t in tasks:
            tasks.remove(t)

    else:
        break