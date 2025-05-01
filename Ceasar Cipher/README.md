# Caesar Cipher

This Python script (`main.py`) implements the Caesar cipher, a simple method of encryption that shifts each letter in a text by a fixed number of positions down the alphabet.

## Description

The Caesar cipher works by replacing each letter with the letter a certain number of positions down the alphabet. For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.  The script allows the user to both encode (encrypt) and decode (decrypt) text using this cipher.

### Key Features

* **Encryption:** Shifts letters forward in the alphabet.
* **Decryption:** Shifts letters backward in the alphabet (effectively the reverse of encryption).
* **User Input:** Prompts the user to enter the text to be encoded/decoded, the shift amount, and whether to encode or decode.
* **Wrap-around:** Handles shifts that go beyond the end of the alphabet (e.g., shifting 'Z' by 1 goes back to 'A').
* **Non-alphabetic Character Handling:** Leaves non-alphabetic characters (e.g., spaces, punctuation) unchanged.
* **Repeated Cipher:** Allows the user to encode/decode multiple messages until they choose to stop.

## How to Use

1.  **Prerequisites:**
    * Python 3.x installed.
2.  **Run the script:**

    ```bash
    python main.py
    ```

3.  **Interaction:**
    * The script will first ask you to type either 'encode' to encrypt a message or 'decode' to decrypt a message.
    * Then, it will ask you to type your message.
    * Finally, it will ask you to type the 'shift number' (the number of positions to shift each letter).
    * The script will then output the encoded or decoded message.
    * It will ask if you want to go again. Type 'yes' to continue or 'no' to exit.

## Code Explanation

* **`alphabet` List:** This list stores the letters of the alphabet twice to handle wrap-around when shifting (e.g., when encoding 'z').
* **`caesar()` Function:**
    * Takes `start_text` (the message), `shift_amount` (the shift value), and `cipher_direction` ('encode' or 'decode') as input.
    * If `cipher_direction` is 'decode', it negates the `shift_amount` to shift backward.
    * Iterates through each character in the `start_text`.
    * If the character is a letter, it finds its `position` in the `alphabet` list, calculates the `new_position` after shifting, and appends the letter at the `new_position` to `end_text`.
    * If the character is not a letter, it appends it directly to `end_text`.
    * Prints the final encoded or decoded `end_text`.
* **Main Loop:**
    * The `while not should_end:` loop continues until the user decides to stop.
    * Inside the loop:
        * It gets user input for `direction`, `text`, and `shift`.
        * It calculates `shift % 26` to ensure the shift value is within the range of the alphabet (0-25).
        * Calls the `caesar()` function to perform the encoding or decoding.
        * Asks the user if they want to restart. If the answer is 'no', `should_end` is set to `True`, and the loop terminates.

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here's the encoded result: mjqqt btwqi
Type 'yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi
Type the shift number:
5
Here's the decoded result: hello world
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye
```

## Dependencies

* Python 3.x
