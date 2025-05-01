from tkinter import *
from tkinter import messagebox


def checkvalue():
    try:
        float(entry.get())
    except ValueError:
        messagebox.showinfo(title="Warning", message="Kindly make sure that the entry is not empty \n"
                                                     "Enter integers only")


def change_value(c, f, k):
    ans1_label.config(text=f"The temperature in celcius is {c}")
    ans2_label.config(text=f"The temperature in Farenheit is {f}")
    ans3_label.config(text=f"The temperature in Kelvin is {k}")


def celcius_converter():
    checkvalue()
    c = float(entry.get())
    f = round((9/5)*c, 2) + 32
    k = c + 273.15
    change_value(c, f, k)


def farenheit_converter():
    checkvalue()
    f = float(entry.get())
    c = round((f - 32) * 5 / 9, 2)
    k = c + 273.15
    change_value(c, f, k)


def kelvin_converter():
    checkvalue()
    k = float(entry.get())
    c = k - 273.15
    f = round((9 / 5) * c + 32, 2)
    change_value(c, f, k)


# Creating a window #
window = Tk()
window.title("Temperature Converter")
window.minsize(width=500, height=400)
window.config(bg='lightblue')

# Creating Labels and buttons#
title_label = Label(text="Welcome to temperature converter", font=("Arial", 30, "bold"))
title_label.config(bg='lightblue')
title_label.grid(row=0, column=1)

# Creating all the labels
label_1 = Label(text="Press 1. If you want to change from celcius to Fahrenheit and kelvin",
                font=("Arial", 10, "bold"),
                bg='yellow')
label_1.grid(row=1, column=1)

label_2 = Label(text="Press 2. If you want to change from Farenheit to celcius and Kelvin",
                font=("Arial", 10, "bold"),
                bg='light green')
label_2.grid(row=2, column=1)

label_3 = Label(text="Press 3. If you want to convert from Kelvin to Farenheit and Celcius",
                font=("Arial", 10, "bold"),
                bg='red',
                fg='white')
label_3.grid(row=3, column=1)

value_label = Label(text="Enter the value.",
                    font=("Arial", 20, "bold"),
                    bg='lightblue')
value_label.grid(row=4, column=0)

# Creating entry#
entry = Entry(width=40, font=("Arial", 15, "bold"))
entry.grid(row=4, column=1)
entry.focus()

# Creating Buttons
button_1 = Button(text="1", font=("Arial", 10, "bold"), width=20, bg='yellow', command=celcius_converter)
button_1.grid(row=5, column=0)

button_2 = Button(text="2", font=("Arial", 10, "bold"), width=20, bg='lightgreen', command=farenheit_converter)
button_2.grid(row=5, column=1)

button_3 = Button(text="3", font=("Arial", 10, "bold"), width=20, bg='red', command=kelvin_converter)
button_3.grid(row=5, column=2)

# Creating the answer labels
ans1_label = Label(text="", font=("Arial", 15, "bold"), bg='lightblue')
ans1_label.grid(row=6, column=1)

ans2_label = Label(text="", font=("Arial", 15, "bold"), bg='lightblue')
ans2_label.grid(row=7, column=1)

ans3_label = Label(text="", font=("Arial", 15, "bold"), bg='lightblue')
ans3_label.grid(row=8, column=1)

window.mainloop()
