#2.	Design a GUI based basic calculator for performing basic arithmetic operations.
import tkinter as tk
def press(x):
    e.insert(tk.END, x)
def clear():
    e.delete(0, tk.END)
def calc():
    try:
        ans = eval(e.get())
        e.delete(0, tk.END)
        e.insert(0, ans)
    except:
        e.delete(0, tk.END)
        e.insert(0, "error")
root = tk.Tk()
root.title("Calculator")
e = tk.Entry(root, width=20)
e.grid(row=0, column=0, columnspan=4)
btns = ['7','8','9','/',
        '4','5','6','*',
        '1','2','3','-',
        '0','.','=','+']
r = 1
c = 0
for i in btns:
    if i == '=':
        tk.Button(root, text=i, width=5, command=calc).grid(row=r, column=c)
    else:
        tk.Button(root, text=i, width=5, command=lambda x=i: press(x)).grid(row=r, column=c)
    c += 1
    if c == 4:
        c = 0
        r += 1
tk.Button(root, text="C", width=20, command=clear).grid(row=r, column=0, columnspan=4)
root.mainloop()