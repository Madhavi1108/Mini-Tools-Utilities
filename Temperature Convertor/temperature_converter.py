#Declaring a function to initialize the values in Celcius , Farenheit and Kelvin
def tempertaure_converter():
    def value():
        c = 0
        f = 0
        k = 0

#Declaring a function to convert celcius to farenheight and kelvin
    def celcius_converter(b):
        value()
        f = (9/5)*b + 32
        k = b + 273.15
        print(f"The temperature in Farenheit is{f}")
        print(f"The temperature in Kelvin is{k}")

# Declaring a function to convert farenheight to celcius and kelvin
    def farenheit_converter(b):
        value()
        c = (b-32)*5/9
        k = c + 273.15
        print(f"The temperature in Celcius is{c}")
        print(f"The temperature in Kelvin is{k}")

# Declaring a function to convert kelvin to celcius and farenheit
    def kelvin_converter(b):
        value()
        c = b - 273.15
        f = (9 / 5) * c + 32
        print(f"The temperature in Celcius is{c}")
        print(f"The temperature in Farenheit is{f}")

#Declaring a function to ensure that the user can reuse the code as long as he wishes
    def is_function():
        if input("Would you like to use the temperature converter again?").upper() == 'YES':
            tempertaure_converter()
        else:
            print("Thank you for choosing the converter")
            exit(0)

#Ensuring that the functions are called correctly based on the user input
    def choosing_number(a,b):
        if a == 1:
            celcius_converter(b)
            is_function()

        elif a == 2:
            farenheit_converter(b)
            is_function()

        elif a == 3 :
            kelvin_converter(b)
            is_function()

        else:
            print("Kindly enter numbers between 1 to 3")
            is_function()

    a = int(input('Press 1. if you want to change celcius to Farenheit and kelvin.\n'
                  'Press 2. If you want to change Farenheit \n'
                  'Press 3. If you want to convert Kelvin to Farenheit and Celcius\n'))

    b = float(input("Enter the temperature value"))

    choosing_number(a, b)

print("Welcome to temperature converter")
tempertaure_converter()
