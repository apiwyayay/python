"""
Author: Ravy Ardian Kusuma (apiwyayay)
Created: 2024-01-09

Title: Temperature Converter
"""

from tkinter import *
import tkinter.font

root = Tk()
root.title("TempConverter")
root.geometry("400x400")

# set font size
thefont = tkinter.font.Font(size=15)

# create a new frame
newframe = LabelFrame(root, text="Temp Converter", padx=10, pady=10)
newframe.place(x=15, y=10)

# title and equal sign
title = Label(newframe, text="Temperatur").grid(row=0, columnspan=3)
equals_sign = Label(newframe, text="=").grid(row=1, column=1)

# create number input boxes
e1 = Entry(newframe,width=15)
e2 = Entry(newframe,width=15)
e1["font"] = thefont
e2["font"] = thefont
e2.insert(0, "0")
e1.grid(row=1, column=0)
e2.grid(row=1, column=2)

# write the formula and all functions
formula_lbl = Label(newframe, text="Formula", bg="yellow")
formula_lbl.place(x=1, y=90)

formula_text = Label(newframe,text="(...°C x 9/5) + 32 = ... °F")
formula_text.place(x=50, y=90)

check = {"formula","yes"}

def calculate(formula):
    # delete text in box 2
    e2.delete(0, END)

    # get values from the boxes
    box_one = clicked.get()
    box_two = clicked2.get()
    number_one = int(e1.get())

    # remove previous text
    global formula_text
    if "formula" in check:
        formula_text.place_forget()
    else:
        pass

    # write the formula and determine calculation
    if box_one == "Celcius" and box_two == "Fahrentheit":
        formula_text = Label(newframe, text="("+e1.get()+"°C * 9/5) + 32 = ... °F")
        calculation = (number_one * 9/5) + 32
    elif box_one == "Celcius" and box_two == "Kelvin":
        formula_text = Label(newframe,text=e1.get()+"°C + 273.15 = ... °K")
        calculation = (number_one + 273.15)
    elif box_one == "Celcius" and box_two == "Reamur":
        formula_text = Label(newframe,text="(4/5 * "+e1.get()+"°C) = ... °R")
        calculation = (4/5 * number_one)
    elif box_one == "Fahrentheit" and box_two == "Celcius":
        formula_text = Label(newframe,text="("+e1.get()+"°F - 32) * 5/9 = ... °C")
        calculation = (number_one - 32) * 5/9
    elif box_one == "Fahrentheit" and box_two == "Kelvin":
        formula_text = Label(newframe,text="("+e1.get()+"°F - 32) * 5/9 + 273.15 = ... °K")
        calculation = (number_one - 32) * 5/9 + 273.15
    elif box_one == "Fahrentheit" and box_two == "Reamur":
        formula_text = Label(newframe,text="("+e1.get()+"°F - 32) * 4/9 = ... °R")
        calculation = (number_one - 32) * 4/9
    elif box_one == "Reamur" and box_two == "Celcius":
        formula_text = Label(newframe,text="5/4 * "+e1.get()+"R) = ... °C")
        calculation = (5/4 * number_one)
    elif box_one == "Reamur" and box_two == "Fahrentheit":
        formula_text = Label(newframe,text="(9/4 * "+e1.get()+"R) + 32 = ... °F")
        calculation = (9/4 * number_one) + 32
    elif box_one == "Reamur" and box_two == "Kelvin":
        formula_text = Label(newframe,text="(5/4 *"+e1.get()+"R) + 273 = ... °K")
        calculation = (5/4 * number_one) + 273
    elif box_one == "Kelvin" and box_two == "Celcius":
        formula_text = Label(newframe,text=e1.get()+"°K - 273.15 = ... °C")
        calculation = (number_one - 273.15)
    elif box_one == "Kelvin" and box_two == "Fahrentheit":
        formula_text = Label(newframe,text="("+e1.get()+"°K - 273.15) * 9/5 + 32 = ... °F ")
        calculation = (number_one - 273.15) * 9/5 + 32 
    elif box_one == "Kelvin" and box_two == "Reamur":
        formula_text = Label(newframe,text="("+e1.get()+"°K - 273) * 4/5 = ... °R")
        calculation = (number_one - 273) * 4/5
    elif box_one == "Celcius" and box_two == "Celcius" or box_one == "Fahrentheit" and box_two == "Fahrentheit" or  box_one == "Reamur" and box_two == "Reamur" or box_one == "Kelvin" and box_two == "Kelvin" :
        formula_text = Label(newframe,text="No Formula Available")
        calculation = number_one
    result = calculation
    e2.insert(0, result)
    formula_text.place(x=50, y=90)

# input values for temperature options
options = ["Celcius", "Fahrentheit", "Kelvin", "Reamur"]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(newframe, clicked, *options, command=calculate)
drop.config(width=20)
drop.grid(row=2, column=0)

clicked2 = StringVar()
clicked2.set(options[1])
drop2 = OptionMenu(newframe, clicked2, *options, command=calculate)
drop2.config(width=20)
drop2.grid(row=2, column=2)

# create a button to calculate
btn = Button(newframe, text="Count", command=lambda: calculate("calculate"))
btn.grid(row=3, column=2)

root.mainloop()