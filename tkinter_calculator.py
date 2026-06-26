# =========================================
# Topic : Simple Calculator using Tkinter
# =========================================

from tkinter import *

# =========================================
# Window
# =========================================

root = Tk()

root.title("Simple Calculator")

root.geometry("350x450")

# =========================================
# Entry Box
# =========================================

e = Entry(

    root,

    font=("Arial", 25),

    bd=10,

    justify="right"
)

e.pack(fill=BOTH, padx=10, pady=10)

# =========================================
# Functions
# =========================================

def click(num):

    e.insert(END, str(num))


def clear():

    e.delete(0, END)


def equal():

    try:

        result = eval(e.get())

        e.delete(0, END)

        e.insert(0, result)

    except:

        e.delete(0, END)

        e.insert(0, "Error")

# =========================================
# Buttons Frame
# =========================================

f = Frame(root)

f.pack()

# Row 1
Button(f, text="7", width=8, height=3,
       command=lambda: click(7)).grid(row=0, column=0)

Button(f, text="8", width=8, height=3,
       command=lambda: click(8)).grid(row=0, column=1)

Button(f, text="9", width=8, height=3,
       command=lambda: click(9)).grid(row=0, column=2)

Button(f, text="/", width=8, height=3,
       command=lambda: click("/")).grid(row=0, column=3)

# Row 2
Button(f, text="4", width=8, height=3,
       command=lambda: click(4)).grid(row=1, column=0)

Button(f, text="5", width=8, height=3,
       command=lambda: click(5)).grid(row=1, column=1)

Button(f, text="6", width=8, height=3,
       command=lambda: click(6)).grid(row=1, column=2)

Button(f, text="*", width=8, height=3,
       command=lambda: click("*")).grid(row=1, column=3)

# Row 3
Button(f, text="1", width=8, height=3,
       command=lambda: click(1)).grid(row=2, column=0)

Button(f, text="2", width=8, height=3,
       command=lambda: click(2)).grid(row=2, column=1)

Button(f, text="3", width=8, height=3,
       command=lambda: click(3)).grid(row=2, column=2)

Button(f, text="-", width=8, height=3,
       command=lambda: click("-")).grid(row=2, column=3)

# Row 4
Button(f, text="0", width=8, height=3,
       command=lambda: click(0)).grid(row=3, column=0)

Button(f, text="C", width=8, height=3,
       command=clear).grid(row=3, column=1)

Button(f, text="=", width=8, height=3,
       command=equal).grid(row=3, column=2)

Button(f, text="+", width=8, height=3,
       command=lambda: click("+")).grid(row=3, column=3)

# =========================================
# Run Window
# =========================================

root.mainloop()