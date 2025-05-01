FONT_Text = ("Arial", 15, "bold")


def tip_calculator():
    bill = bill_entry.get()
    tip_percentage = tip_percentage_entry.get()
    people = people_entry.get()

    try:
        bill = int(bill)
        tip_percentage = int(tip_percentage)
        people = int(people)
    except ValueError:
        messagebox.showinfo(title="Warning", message="Kindly make sure that the entry is not empty \n"
                                                     "Enter integers only")
    else:
        if bill != 0 and tip_percentage != 0 and people != 0:
            if tip_percentage == 10 or tip_percentage == 12 or tip_percentage == 15:
                tip_amount = bill * tip_percentage / (people * 100)
                answer_label = Label(text=f"Each person has to pay a tip of {tip_amount}$",
                                     font=FONT_Text, bg='lightblue')
                answer_label.grid(row=5, column=0, columnspan=3)
            else:
                messagebox.showinfo(title="Warning", message="Kindly enter only 10, 12 or 15 as the tip percentage")
        else:
            messagebox.showinfo(title="Warning",message="Kindly make sure that none of the entries are zero")



# Creating a window
window = Tk()
window.title("My tip calculator")
window.minsize(width=500, height=450)
window.config(bg='lightblue')

# Creating title label
title_label = Label(text="Welcome to tip calculator", font=("Arial", 30, "bold"))
title_label.config(bg='lightblue')
title_label.grid(row=0, column=0, columnspan=3)

# Creating the bill label and entry
bill_label = Label(text="Enter the bill", font=FONT_Text, bg='lightblue')
bill_label.grid(row=1, column=0)

bill_entry = Entry(width=40, font=FONT_Text)
bill_entry.grid(row=1, column=1)
bill_entry.focus()

# Creating the tip percentage label and entry
tip_percentage_label = Label(text="Kindly enter the tip percentage as 10, 12 or 15 ",
                             font=FONT_Text, bg='lightblue')
tip_percentage_label.grid(row=2, column=0)

tip_percentage_entry = Entry(width=40, font=FONT_Text)
tip_percentage_entry.grid(row=2, column=1)

# Creating the people label and entry
people_label = Label(text="Kindly enter the number of people who will share the bill", font=FONT_Text, bg='lightblue')
people_label.grid(row=3, column=0)

people_entry = Entry(width=40, font=FONT_Text)
people_entry.grid(row=3, column=1)

# Creating the calculate button
calculate_button = Button(text="Calculate", font=FONT_Text,
                          width=20, bg='yellow',
                          command=tip_calculator)
calculate_button.grid(row=4, column=0, columnspan=2)

for i in range(1, 4):
    currency_label = Label(text="$", font=FONT_Text, bg='lightblue')
    currency_label.grid(row=i, column=3)

window.mainloop()
