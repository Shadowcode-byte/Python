#5.	Design a login and signup authentication system.
import tkinter as tk
import sqlite3
con = sqlite3.connect("user.db")
cur = con.cursor()
cur.execute("create table if not exists u(name text, pass text)")
con.commit()
def signup():
    a = e1.get()
    b = e2.get()
    cur.execute("insert into u values(?,?)", (a,b))
    con.commit()
    print("signup done")
def login():
    a = e1.get()
    b = e2.get()

    cur.execute("select * from u where name=? and pass=?", (a,b))
    r = cur.fetchone()

    if r:
        print("login success")
    else:
        print("wrong")

root = tk.Tk()
root.title("Login")

tk.Label(root, text="User").grid(row=0)
tk.Label(root, text="Pass").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root, show="*")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(root, text="Signup", command=signup).grid(row=2, column=0)
tk.Button(root, text="Login", command=login).grid(row=2, column=1)

root.mainloop()