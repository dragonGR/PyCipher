# PyCipher

PyCipher is a simple password generator app built in Python. It allows you to generate random passwords of customizable length, with options to include digits and symbols. The app provides a command-line interface for ease of use.

## Features
- Generate strong passwords with customizable length.
- Include digits, symbols, and custom characters for enhanced security.
- Exclude ambiguous characters for better readability.
- User-friendly interface with clear prompts and error handling.
- Basic password strength check for additional security awareness.
- Improved code structure and readability.

## Requirements

- Python 3.x

## Usage
1. Clone the repository or download the `pycipher.py` file.

2. Open a terminal or command prompt and navigate to the directory where `pycipher.py` is located.

3. Run the following command to execute the PyCipher app:

```
python pycipher.py
```

4. Follow the prompts to define your desired password length, character inclusion options.

5. The generated password will be displayed on the screen.

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
- Advanced password strength checks.
- Password management features (optional).
- Graphical user interface (optional).
- More robust error handling and informative messages.
- Unit tests for code correctness.
- Logging functionality for error tracking.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
