from tkinter import *
from tkinter import messagebox

bg_color = "#787878"

def zero_button_fonction():
    input.insert(END, "0")

def one_button_fonction():
    input.insert(END, "1")

def two_button_fonction():
    input.insert(END, "2")

def three_button_fonction():
    input.insert(END, "3")

def four_button_fonction():
    input.insert(END, "4")

def five_button_fonction():
    input.insert(END, "5")

def six_button_fonction():
    input.insert(END, "6")

def seven_button_fonction():
    input.insert(END, "7")

def eight_button_fonction():
    input.insert(END, "8")

def nine_button_fonction():
    input.insert(END, "9")

def delete_function():
    input.delete(len(input.get())-1, END)

def mult_button_fonction():
    input.insert(END, "*")

def div_button_fonction():
    input.insert(END, "/")

def plus_button_fonction():
    input.insert(END, "+")

def sub_button_fonction():
    input.insert(END, "-")

def equal_button_fonction():
    expression = input.get()

    try:
        result = eval(expression)

        input.delete(0, END)
        input.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid expression")
    

root = Tk()
root.configure(background=bg_color)
root.geometry("700x650")

input_grid = Frame(root, bg=bg_color)

input = Entry(input_grid, bg=bg_color, fg="black", font=("Helvetica", 30), width=10, border=0)
input.grid(row=0, column=0, sticky=W)

remove = PhotoImage(file="Assets/remove.png")
remove_button = Button(input_grid, image=remove, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=delete_function)
remove_button.grid(row=0, column=1, sticky=W)

input_grid.pack(expand=YES)

sign_grid = Frame(root, background=bg_color)

nine = PhotoImage(file='Assets/number-9.png')
nine_button = Button(sign_grid, image=nine, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=nine_button_fonction)
nine_button.grid(row=0, column=0, sticky=W)

height = PhotoImage(file='Assets/number-8.png')
height_button = Button(sign_grid, image=height, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=eight_button_fonction)
height_button.grid(row=0, column=1, sticky=W)

seven = PhotoImage(file='Assets/seven.png')
seven_button = Button(sign_grid, image=seven, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=seven_button_fonction)
seven_button.grid(row=0, column=2, sticky=W)

six = PhotoImage(file='Assets/six.png')
six_button = Button(sign_grid, image=six, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=six_button_fonction)
six_button.grid(row=1, column=0, sticky=W)

five = PhotoImage(file='Assets/number-5.png')
five_button = Button(sign_grid, image=five, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=five_button_fonction)
five_button.grid(row=1, column=1, sticky=W)

four = PhotoImage(file='Assets/number-four.png')
four_button = Button(sign_grid, image=four, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=four_button_fonction)
four_button.grid(row=1, column=2, sticky=W)

three = PhotoImage(file='Assets/number-3.png')
three_button = Button(sign_grid, image=three, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=three_button_fonction)
three_button.grid(row=2, column=0, sticky=W)

two = PhotoImage(file='Assets/number-2.png')
two_button = Button(sign_grid, image=two, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=two_button_fonction)
two_button.grid(row=2, column=1, sticky=W)

one = PhotoImage(file='Assets/number-one.png')
one_button = Button(sign_grid, image=one, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=one_button_fonction)
one_button.grid(row=2, column=2, sticky=W)

zero = PhotoImage(file='Assets/zero.png')
zero_button = Button(sign_grid, image=zero, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=zero_button_fonction)
zero_button.grid(row=3, column=1, sticky=W)

plus = PhotoImage(file="Assets/plus.png")
plus_button = Button(sign_grid, image=plus, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=plus_button_fonction)
plus_button.grid(row=0, column=3, sticky=W)

multiply = PhotoImage(file="Assets/multiply.png")
multiply_button = Button(sign_grid, image=multiply, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=mult_button_fonction)
multiply_button.grid(row=1, column=3, sticky=W)

divide = PhotoImage(file="Assets/divide.png")
divide_button = Button(sign_grid, image=divide, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=div_button_fonction)
divide_button.grid(row=2, column=3, sticky=W)

equal = PhotoImage(file="Assets/equal.png")
equal_button = Button(sign_grid, image=equal, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=equal_button_fonction)
equal_button.grid(row=3, column=3, sticky=W)

sign_grid.pack(expand=YES)

root.mainloop()