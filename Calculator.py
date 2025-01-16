---------------------
# Name:        module2
# Purpose:
#
# Author:      Ashirbad Sahani
#
# Created:     09-07-2024
# Copyright:   (c) Ashirbad Sahani 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""

@Author: Ashirbad Sahani
Institute: ITER, SOA
Language: Python
Version: 3.x
Platform: Pycharm Community Version

"""

from tkinter import *;
from tkinter import messagebox;

def actionauthor():
    messagebox.showinfo("Author", "Ashirbad Sahani\nBatch: 7th sem\nDepartment: CSE\nITER, SOA")

# Check whether the input string is a number or not
def is_number(s):
    if(s != ''):
        if (s.replace('.', '', 1).isdigit()):
            return True
        if (s.isdigit()):
            return True;
        if s[0] in ['-', '+', '.', '0', ' ']:
            if (s[1] == '.'):
                if (s[2:].isdigit()):
                    return True
            if (s[1] == '0' and s[2] == '.'):
                if (s[3:].isdigit()):
                    return True
            if s[1:].isdigit():
                return True;
        return False;

def casting(num):
    if('.' in num):
        return float(num);
    else:
        return int(num)

def clear_entries():
    Numberentry1.delete(0, END)
    Operatorentry.delete(0, END)
    Numberentry2.delete(0, END)
    Showlabel.delete(0, END)

def calculate():
    try:
        num1 = casting(Numberentry1.get())
        num2 = casting(Numberentry2.get())
        operator = Operatorentry.get()
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        Showlabel.delete(0, END)
        Showlabel.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")

def insert_number(num):
    if Numberentry1.focus_get() == Numberentry1:
        current = Numberentry1.get()
        Numberentry1.delete(0, END)
        Numberentry1.insert(0, current + num)
    elif Numberentry2.focus_get() == Numberentry2:
        current = Numberentry2.get()
        Numberentry2.delete(0, END)
        Numberentry2.insert(0, current + num)

def insert_operator(operator):
    Operatorentry.delete(0, END)
    Operatorentry.insert(0, operator)

root = Tk();
root.title('My First Python Calculator');
root.geometry('300x400+200+250');
root.configure(bg='pink')

clearbutton = Button(root, text='Clear', width=6, command=clear_entries)
clearbutton.place(relx=0.1, rely=0.05, anchor='center')

authorbutton = Button(root, text='Author', width=6, command=actionauthor)
authorbutton.place(relx=0.9, rely=0.05, anchor='center')

Titlelabel = Label(root, fg='green', font='none 10 bold underline', text='Python Calculator', bg='pink')
Titlelabel.place(relx=0.5, rely=0.1, anchor='center')

input1_label = Label(root, text="Enter first number:", bg='pink')
input1_label.place(relx=0.5, rely=0.15, anchor='center')
Numberentry1 = Entry(root)
Numberentry1.place(relx=0.5, rely=0.2, anchor='center')

operator_label = Label(root, text="Enter operator:", bg='pink')
operator_label.place(relx=0.5, rely=0.25, anchor='center')
Operatorentry = Entry(root)
Operatorentry.place(relx=0.5, rely=0.3, anchor='center')

input2_label = Label(root, text="Enter second number:", bg='pink')
input2_label.place(relx=0.5, rely=0.35, anchor='center')
Numberentry2 = Entry(root)
Numberentry2.place(relx=0.5, rely=0.4, anchor='center')

result_label = Label(root, text="Result:", bg='pink')
result_label.place(relx=0.5, rely=0.45, anchor='center')
Showlabel = Entry(root)
Showlabel.place(relx=0.5, rely=0.5, anchor='center')

buttons = [
    ('1', 0.1, 0.6), ('2', 0.3, 0.6), ('3', 0.5, 0.6), ('+', 0.7, 0.6),
    ('4', 0.1, 0.7), ('5', 0.3, 0.7), ('6', 0.5, 0.7), ('-', 0.7, 0.7),
    ('7', 0.1, 0.8), ('8', 0.3, 0.8), ('9', 0.5, 0.8), ('*', 0.7, 0.8),
    ('0', 0.1, 0.9), ('.', 0.3, 0.9), ('=', 0.5, 0.9), ('/', 0.7, 0.9)
]

for (text, x, y) in buttons:
    if text == '=':
        Button(root, text=text, width=5, command=calculate).place(relx=x, rely=y)
    else:
        Button(root, text=text, width=5, command=lambda t=text: insert_number(t) if t not in ['+', '-', '*', '/'] else insert_operator(t)).place(relx=x, rely=y)

root.resizable(False, False)
root.mainloop()
