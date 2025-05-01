print("Welcome to tip calculator")


def is_amount_correct():
    amount = input("What was the total bill? :$")
    try:
        amount = float(amount)
    except ValueError:
        print("Kindly do not leave any spaces empty and fill integers only")
        correct_amount = is_amount_correct()
        return correct_amount
    else:
        if amount != 0:
            return amount
        else:
            print("Kindly enter your bill")
            correct_amount = is_amount_correct()
            return correct_amount


def is_tip_correct():
    tip_percentage = input("How much tip would you like to give? 10, 12 or 15 : ")
    try:
        tip_percentage = float(tip_percentage)
    except ValueError:
        print("Kindly do not leave any spaces empty and fill integers only")
        correct_tip_percentage = is_tip_correct()
        return correct_tip_percentage
    else:
        if tip_percentage == 10 or tip_percentage == 12 or tip_percentage == 15:
            return tip_percentage
        else:
            print("Kindly enter the tip percentage as 10, 12 or 15 ")
            correct_tip_percentage = is_tip_correct()
            return correct_tip_percentage


def are_people_correct():
    people = input("How many people would split the bill? ")
    try:
        people = float(people)
    except ValueError:
        print("Kindly do not leave any spaces empty and fill integers only")
        people = are_people_correct()
        return people
    else:
        if people != 0:
            return people
        else:
            print("Kindly enter how many people are splitting the bill")
            people = are_people_correct()
            return people


bill = is_amount_correct()
tip = is_tip_correct()
persons = are_people_correct()

tip_amount = round(bill * tip/(100 * persons), 2)
print(f"Each person has to pay a tip of ${tip_amount}")
