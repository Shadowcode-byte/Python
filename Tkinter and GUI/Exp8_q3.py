#3.	Design a GUI for student registration for a course and store these details in a database. 
# Use Tkinter for UI, SQLite/MySQL for database storage.
import tkinter as tk
import sqlite3
con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("create table if not exists student(name text, course text)")
con.commit()
def save():
    n = e1.get()
    c = e2.get()

    cur.execute("insert into student values(?,?)", (n,c))
    con.commit()
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
root = tk.Tk()
root.title("Register")
tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Course").grid(row=1)
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(root, text="Submit", command=save).grid(row=2, column=1)
root.mainloop()