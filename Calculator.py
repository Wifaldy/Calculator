from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, "end")


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, "end")
    print(math)


def button_equal():
    second_number = e.get()
    e.delete(0, "end")
    if math == "addition":
        e.insert(0, f_num+int(second_number))
    elif math == "substraction":
        e.insert(0, f_num-int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num*int(second_number))
    elif math == "division":
        e.insert(0, f_num/int(second_number))


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, "end")


def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, "end")


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, "end")


button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: click(0))
button_add = Button(root, text="+", padx=29, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=70, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=60,
                      pady=20, command=button_clear)
button_sub = Button(root, text="-", padx=30, pady=20, command=button_sub)
button_mult = Button(root, text="*", padx=31, pady=20, command=button_mult)
button_div = Button(root, text="/", padx=31, pady=20, command=button_div)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(columnspan=2, row=4, column=1)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, columnspan=2, column=1)
button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)


root.mainloop()
