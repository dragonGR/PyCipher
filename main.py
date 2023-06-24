import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True, exclude_ambiguous=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if exclude_ambiguous:
        ambiguous_characters = 'l1O0'
        characters = ''.join(c for c in characters if c not in ambiguous_characters)

    try:
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    except ValueError:
        print("Error: Invalid password length.")
        return None

def main():
    try:
        length = int(input("Enter the desired password length: "))
        include_digits = input("Include digits (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols (y/n): ").lower() == 'y'
        exclude_ambiguous = input("Exclude ambiguous characters (e.g., 'l', '1', 'O', '0') (y/n): ").lower() == 'y'

        password = generate_password(length, include_digits, include_symbols, exclude_ambiguous)

        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Error: Invalid input. Please enter a valid length.")
    except KeyboardInterrupt:
        print("\nPassword generation interrupted.")

if __name__ == '__main__':
    main()
