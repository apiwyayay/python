"""
Author: Ravy Ardian Kusuma (apiwyayay)
Created: 2024-01-12

Title: Time Converter
"""

from tkinter import *
import tkinter.font

class TimeUnit:
    def __init__(self, name, seconds_per_unit):
        self.name = name
        self.seconds_per_unit = seconds_per_unit

    def convert_to_seconds(self, value):
        return int(value * self.seconds_per_unit)

    def convert_from_seconds(self, value):
        return int(value / self.seconds_per_unit)

root = Tk()
root.title("Time Converter")
root.geometry("400x400")

# set font size
thefont = tkinter.font.Font(size=15)

# create a new frame
time_frame = LabelFrame(root, text="Time Converter", padx=10, pady=10)
time_frame.place(x=15, y=10)

# title and equal sign
title = Label(time_frame, text="Time").grid(row=0, columnspan=3)
equals_sign = Label(time_frame, text="=").grid(row=1, column=1)

# create number input boxes
e1 = Entry(time_frame, width=15)
e2 = Entry(time_frame, width=15)
e1["font"] = thefont
e2["font"] = thefont
e2.insert(0, "0")
e1.grid(row=1, column=0)
e2.grid(row=1, column=2)

# # write the formula and all functions
# formula_lbl = Label(time_frame, text="Formula", bg="yellow")
# formula_lbl.place(x=1, y=90)

# formula_text = Label(time_frame, text="(... Millennium) = ... Seconds")
# formula_text.place(x=50, y=90)

check = {"formula", "yes"}

# Initialize time units
millennium = TimeUnit("Millennium", 1000 * 365 * 24 * 60 * 60)
centuries = TimeUnit("Centuries", 100 * 365 * 24 * 60 * 60)
decades = TimeUnit("Decades", 10 * 365 * 24 * 60 * 60)
windu = TimeUnit("Windu", 8 * 365 * 24 * 60 * 60)
lustrum = TimeUnit("Lustrum", 5 * 365 * 24 * 60 * 60)
years = TimeUnit("Years", 365 * 24 * 60 * 60)
months = TimeUnit("Months", 30 * 24 * 60 * 60)
quadrenniums = TimeUnit("Quadrenniums", 4 * months.seconds_per_unit)
quarters = TimeUnit("Quarters", 3 * months.seconds_per_unit)
weeks = TimeUnit("Weeks", 7 * 24 * 60 * 60)
days = TimeUnit("Days", 24 * 60 * 60)
hours = TimeUnit("Hours", 60 * 60)
minutes = TimeUnit("Minutes", 60)
seconds = TimeUnit("Seconds", 1)

time_units = [millennium, centuries, decades, windu, lustrum, years, months, quadrenniums, quarters, weeks, days, hours, minutes, seconds]

def calculate(formula):
    # delete text in box 2
    e2.delete(0, END)

    # get values from the boxes
    box_one = clicked.get()
    box_two = clicked2.get()
    number_one = int(e1.get())

    # # remove previous text
    # global formula_text
    # if "formula" in check:
    #     formula_text.place_forget()
    # else:
    #     pass

    # write the formula and determine calculation
    for unit in time_units:
        if box_one == unit.name and box_two in [u.name for u in time_units]:
            target_unit = next(u for u in time_units if u.name == box_two)
            # formula_text = Label(time_frame, text=f"({e1.get()} {unit.name}) = ... {box_two}")
            calculation = target_unit.convert_from_seconds(unit.convert_to_seconds(number_one))

    result = calculation
    e2.insert(0, result)
    # formula_text.place(x=50, y=90)

# input values for time options
options = [unit.name for unit in time_units]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(time_frame, clicked, *options, command=calculate)
drop.config(width=20)
drop.grid(row=2, column=0)

clicked2 = StringVar()
clicked2.set(options[-1])
drop2 = OptionMenu(time_frame, clicked2, *options, command=calculate)
drop2.config(width=20)
drop2.grid(row=2, column=2)

# create a button to calculate
btn = Button(time_frame, text="Count", command=lambda: calculate("calculate"))
btn.grid(row=3, column=2)

root.mainloop()
