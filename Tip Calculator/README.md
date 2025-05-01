# Tip Calculator

This repository contains two versions of a tip calculator:

* **`tip.py`**: A command-line version of the tip calculator.
* **`tip calculator using tkinter.py`**: A graphical user interface (GUI) version of the tip calculator built with Tkinter.

## `tip.py` - Command-Line Tip Calculator

### Description

The `tip.py` script is a simple command-line tool that calculates the amount of tip each person has to pay when splitting a bill.  It prompts the user for the total bill amount, the tip percentage (allowing 10, 12, or 15 percent), and the number of people sharing the bill.  It includes error handling to ensure valid input.

### How to Use

1.  Make sure you have Python installed on your system.
2.  Run the script from your terminal:

    ```bash
    python tip.py
    ```

3.  Follow the prompts to enter the bill amount, tip percentage, and the number of people.

### Example

```
Welcome to tip calculator
What was the total bill? :$100
How much tip would you like to give? 10, 12 or 15 : 10
How many people would split the bill? 5
Each person has to pay a tip of $2.0
```

## `tip calculator using tkinter.py` - GUI Tip Calculator

### Description

The `tip calculator using tkinter.py` script provides a user-friendly graphical interface for calculating tips.  It uses the Tkinter library to create a window where users can enter the bill amount, tip percentage (again, only 10, 12, or 15 are accepted), and the number of people.  The calculated tip per person is then displayed in the window.  It also includes error handling with message boxes to inform the user of invalid inputs.

### How to Use

1.  Make sure you have Python installed on your system, including the Tkinter library (Tkinter is usually included with standard Python installations).
2.  Run the script:

    ```bash
    python "tip calculator using tkinter.py"
    ```

3.  A window will appear where you can enter the required information and click the "Calculate" button.

### GUI Elements

* **Title Label**: "Welcome to tip calculator"
* **Bill Entry**:  Entry field to input the total bill amount.
* **Tip Percentage Entry**: Entry field to input the tip percentage (10, 12, or 15).
* **Number of People Entry**: Entry field to input the number of people sharing the bill.
* **Calculate Button**:  Button to trigger the tip calculation.
* **Answer Label**: Label to display the calculated tip amount per person.
* **Currency Labels**:  Labels displaying the '$' symbol.
* **Message Boxes**: Pop-up windows to display warning messages for invalid input.

### Example

*(A screenshot of the GUI would be helpful here)*

## Error Handling

Both versions of the tip calculator include error handling:

* **Invalid Input**:  If the user enters non-numeric values or leaves fields empty, the program will display an error message.
* **Invalid Tip Percentage**:  The program ensures that the tip percentage is either 10, 12, or 15.
* **Zero Values**:  The program checks that the bill amount and the number of people are not zero.

## Dependencies

* **Python 3.x**
* **Tkinter** (for the GUI version - usually included with Python)
```