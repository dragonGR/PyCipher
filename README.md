# PyCipher

PyCipher is a simple password generator app built in Python. It allows you to generate random passwords of customizable length, with options to include digits and symbols. The app provides a command-line interface for ease of use.

## Features
- Generate random passwords of variable length.
- Choose whether to include digits and symbols in the generated passwords.
- Option to exclude ambiguous characters ('l', '1', 'O', '0') that can be easily confused.
- Basic error handling for invalid input and interruptions during password generation.

## Requirements

- Python 3.x

## Usage
1. Clone the repository or download the `pycipher.py` file.

2. Open a terminal or command prompt and navigate to the directory where `pycipher.py` is located.

3. Run the following command to execute the PyCipher app:

```
python pycipher.py
```

4. Follow the prompts to specify the desired password length, inclusion of digits and symbols, and exclusion of ambiguous characters.

5. The app will generate a random password based on your input and display it on the screen.

## Examples

### Example 1: Generating a 10-character password with digits and symbols
**Enter the desired password length**: 10

**Include digits (y/n)**: y

**Include symbols (y/n)**: y

**Exclude ambiguous characters (e.g., 'l', '1', 'O', '0') (y/n)**: n

**Generated Password**: z$6k3B9r1@

### Example 2: Generating a 8-character password without digits and symbols
**Enter the desired password length**: 8

**Include digits (y/n)**: n

**Include symbols (y/n)**: n

**Exclude ambiguous characters (e.g., 'l', '1', 'O', '0') (y/n)**: y

**Generated Password**: eCbLmeWz

## Future Enhancements
- Validation for password length within a reasonable range.
- Improved error handling and informative error messages.
- User interface enhancements such as a graphical interface.
- Unit tests to ensure the correctness of the password generation.
- Logging functionality for error tracking and debugging.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
