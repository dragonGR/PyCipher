import string
import secrets

# Constants
DEFAULT_PASSWORD_LENGTH = 12
DEFAULT_INCLUDE_DIGITS = True
DEFAULT_INCLUDE_SYMBOLS = True
DEFAULT_EXCLUDE_AMBIGUOUS = True

def generate_password(length=DEFAULT_PASSWORD_LENGTH, include_digits=DEFAULT_INCLUDE_DIGITS, include_symbols=DEFAULT_INCLUDE_SYMBOLS, exclude_ambiguous=DEFAULT_EXCLUDE_AMBIGUOUS):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if exclude_ambiguous:
        ambiguous_characters = 'l1IiL0Oo'
        characters = ''.join(c for c in characters if c not in ambiguous_characters)

    try:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password
    except ValueError:
        print("Error: Invalid password length.")
        return None

def main():
    try:
        length = int(input("Enter the desired password length (default is {}): ".format(DEFAULT_PASSWORD_LENGTH)))

        if length <= 0:
            raise ValueError("Invalid input. Password length must be a positive integer.")

        include_digits = input("Include digits (y/n, default is {}): ".format("y" if DEFAULT_INCLUDE_DIGITS else "n")).lower() == 'y'
        include_symbols = input("Include symbols (y/n, default is {}): ".format("y" if DEFAULT_INCLUDE_SYMBOLS else "n")).lower() == 'y'
        exclude_ambiguous = input("Exclude ambiguous characters (e.g., 'l', '1', 'I', 'i', 'O', 'o', '0') (y/n, default is {}): ".format("y" if DEFAULT_EXCLUDE_AMBIGUOUS else "n")).lower() == 'y'

        password = generate_password(length, include_digits, include_symbols, exclude_ambiguous)

        if password:
            print("Generated Password:", password)
    except ValueError as ve:
        print("Error:", str(ve))
    except KeyboardInterrupt:
        print("\nPassword generation interrupted.")

if __name__ == '__main__':
    main()
