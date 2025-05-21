# ☕ Coffee Machine Simulator

This is a simple console-based Coffee Machine Simulator written in Python. It allows users to order drinks, simulates making coffee, checks ingredient sufficiency, and processes payments with coins.

## 📁 Project Structure

```
.
├── Coffeemaker.py       # Manages resources and coffee preparation
├── MENU.py              # Defines menu items and drink data
├── Money_machine.py     # Handles coin input and payment processing
├── new_coffee.py        # Main program that ties everything together
```

## 🚀 Features

* Choose from multiple drinks: **espresso**, **latte**, and **cappuccino**
* Check ingredient levels and profit using the `report` command
* Coin-based payment system that handles change and refunds
* Resource check before making drinks
* Shutdown the machine using the `off` command

## 📦 Requirements

* Python 3.x

No external libraries are needed — it's all standard Python!

## ▶️ How to Run

1. Make sure all the `.py` files are in the same directory.
2. Open your terminal and navigate to the project directory.
3. Run the simulator:

```bash
python new_coffee.py
```

## 📋 Example Interaction

```
What would you like? (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

## 🛠 Code Modules

### `CoffeeMaker`

* Manages water, milk, coffee resources
* Checks if enough ingredients are available
* Makes coffee and updates inventory

### `Menu` & `MenuItem`

* Stores available drinks and their recipes
* Returns options for user prompts
* Finds and returns drink info by name

### `MoneyMachine`

* Accepts coins (quarters, dimes, nickles, pennies)
* Validates payment
* Gives change and tracks profit

## 📌 Notes

* This is a text-based simulation for learning object-oriented programming.
* The coin input simulates physical payment and helps practice conditionals and math.

## 📄 License

This project is open-source and free to use for educational purposes.

