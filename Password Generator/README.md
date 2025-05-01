# Password Generator

This repository contains two Python scripts for generating passwords:

* **`simple_password.py`**:  A basic password generator.
* **`advanced_password.py`**: An enhanced version with shuffled output.

## `simple_password.py` - Simple Password Generator

### Description

The `simple_password.py` script generates passwords based on user-specified criteria. It prompts the user for the desired number of letters, numbers, and symbols in the password.  It ensures the password has a minimum length of 8 characters.  The password is created by concatenating randomly chosen characters, numbers, and symbols.

### How to Use

1.  Ensure you have Python installed.
2.  Run the script:

    ```bash
    python simple_password.py
    ```

3.  Follow the prompts to enter the number of letters, numbers, and symbols.
4.  The script will display the generated password.
5.  You will be prompted if you want to generate another password.

### Example

```
Welcome to 'MY PASSWORD GENERATOR
How many letters you want in your password:3
How many numbers you want in your password:2
How many letters you want in your password:3
Your password is aGT52#$y
Are you satisfied with your password 'yes' or 'no' :no
How many letters you want in your password:4
How many numbers you want in your password:2
How many letters you want in your password:2
Your password is wTU80@q(
Are you satisfied with your password 'yes' or 'no' :yes
```

## `advanced_password.py` - Advanced Password Generator

### Description

The `advanced_password.py` script is similar to `simple_password.py` but with an added feature to enhance password strength. It also prompts the user for the number of letters, numbers, and symbols and ensures a minimum length of 8.  However, after generating the password by combining the character types, it *shuffles* the order of the characters before displaying the final password.  This randomization makes the password more secure against certain types of attacks.

### How to Use

1.  Ensure you have Python installed.
2.  Run the script:

    ```bash
    python advanced_password.py
    ```

3.  Follow the prompts to enter the number of letters, numbers, and symbols.
4.  The script will display the generated (and shuffled) password.
5.  You will be prompted if you want to generate another password.

### Example

```
Welcome to 'MY PASSWORD GENERATOR
How many letters you want in your password:4
How many numbers you want in your password:2
How many letters you want in your password:2
Your password is  %aY5wT8@
Are you satisfied with your password 'yes' or 'no' :yes
```

## Key Features (Both Scripts)

* **Character Sets:** Both scripts use the following character sets:
    * Uppercase letters (A-Z)
    * Lowercase letters (a-z)
    * Numbers (0-9)
    * Symbols: `!@#$%^&*()+`
* **Minimum Length:** Both scripts enforce a minimum password length of 8 characters.
* **User Input:** Both scripts take user input to customize the password complexity.
* **Regeneration Loop:** Both scripts allow the user to regenerate the password if they are not satisfied with the initial one.

## Differences

The crucial difference between the two scripts is the shuffling of the password characters in `advanced_password.py`.  This provides a significant security improvement.

## Dependencies

* Python 3.x
* `random` module (standard Python library - no installation needed)
