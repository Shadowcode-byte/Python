#4.	Create a GUI based task manager where users can add, edit and remove tasks. 
# Use Tkinter (buttons, listbox), SQLite/MySQL (task storage).
import tkinter as tk
import sqlite3
con = sqlite3.connect("task.db")
cur = con.cursor()
cur.execute("create table if not exists t(name text)")
con.commit()
def add():
    x = e.get()
    if x != "":
        lb.insert(tk.END, x)
        cur.execute("insert into t values(?)", (x,))
        con.commit()
        e.delete(0, tk.END)
def delete():
    s = lb.curselection()
    if s:
        val = lb.get(s)
        lb.delete(s)
        cur.execute("delete from t where name=?", (val,))
        con.commit()
def edit():
    s = lb.curselection()
    if s:
        val = lb.get(s)
        new = e.get()
        lb.delete(s)
        lb.insert(s, new)
        cur.execute("update t set name=? where name=?", (new,val))
        con.commit()
root = tk.Tk()
root.title("Task Manager")
e = tk.Entry(root)
e.pack()
tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Edit", command=edit).pack()
lb = tk.Listbox(root)
lb.pack()
tk.Button(root, text="Delete", command=delete).pack()
root.mainloop()