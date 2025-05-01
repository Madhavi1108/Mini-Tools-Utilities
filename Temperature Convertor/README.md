# Unit and Temperature Converter Suite

This repository contains two Python scripts for performing different types of conversions:

* **`converter_using_tkinter.py`**: A versatile unit conversion tool with a graphical user interface (GUI) built using Tkinter.
* **`temperature_converter.py`**: A command-line tool specifically designed for converting temperatures between Celsius, Fahrenheit, and Kelvin.

## `converter_using_tkinter.py` - GUI Unit Converter

### Description

The `converter_using_tkinter.py` script provides a user-friendly graphical interface for converting between various units. It likely supports different categories of conversions (e.g., length, weight, volume, etc.) and allows users to select the input and output units through dropdown menus. The GUI makes the conversion process intuitive and easy to use.

### How to Use

1.  **Prerequisites:**
    * Python 3.x installed
    * Tkinter library (usually included with standard Python installations)
2.  **Run the script:**

    ```bash
    python converter_using_tkinter.py
    ```

3.  **Interface:**
    * A window will appear with options to select the input unit, enter the value to convert, choose the output unit, and a button to trigger the conversion.
    * The converted value will be displayed in the output area.

### Potential Features (Based on common unit converters):

* **Multiple Conversion Types:** Support for length (e.g., meters, feet, inches), weight (e.g., kilograms, pounds, ounces), volume (e.g., liters, gallons, cubic meters), and potentially more.
* **Dropdown Menus:** User-friendly selection of input and output units.
* **Clear Input and Output Fields:** Dedicated areas for entering the value to convert and displaying the result.
* **Error Handling:** Mechanisms to handle invalid input (e.g., non-numeric values).

## `temperature_converter.py` - Command-Line Temperature Converter

### Description

The `temperature_converter.py` script is a command-line tool that allows users to convert temperatures between Celsius, Fahrenheit, and Kelvin. It likely prompts the user for the initial temperature, the original unit, and the desired unit for conversion.

### How to Use

1.  **Prerequisites:**
    * Python 3.x installed
2.  **Run the script:**

    ```bash
    python temperature_converter.py
    ```

3.  **Interaction:**
    * Follow the prompts in the terminal to enter:
        * The temperature value.
        * The original unit (e.g., 'C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin).
        * The desired unit for conversion (e.g., 'F' to convert to Fahrenheit).
    * The script will then output the converted temperature.

### Example

```bash
python temperature_converter.py
Enter the temperature value: 25
Enter the original unit (C, F, K): C
Enter the target unit (C, F, K): F
25.0 Celsius is equal to 77.0 Fahrenheit
```

### Supported Conversions:

* Celsius to Fahrenheit
* Fahrenheit to Celsius
* Celsius to Kelvin
* Kelvin to Celsius
* Fahrenheit to Kelvin
* Kelvin to Fahrenheit

## Dependencies

* **Python 3.x**
* **Tkinter** (for `converter_using_tkinter.py` - usually included with standard Python installations)