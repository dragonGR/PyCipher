import string
import secrets

def generate_password(length=12, include_digits=True, include_symbols=True, exclude_ambiguous=True):
    """Generates a random, secure password based on specified parameters.

    Args:
        length (int): Desired password length (must be positive).
        include_digits (bool): Whether to include digits in the password.
        include_symbols (bool): Whether to include symbols in the password.
        exclude_ambiguous (bool): Whether to exclude ambiguous characters.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If the length is less than 1.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Define character pools
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if exclude_ambiguous:
        ambiguous_chars = 'l1IiL0Oo'
        characters = ''.join(c for c in characters if c not in ambiguous_chars)

    if not characters:
        raise ValueError("No characters available for password generation. Check parameters.")

    return ''.join(secrets.choice(characters) for _ in range(length))

def check_password_strength(password):
    """Evaluates the strength of a given password based on basic criteria.

    Args:
        password (str): The password to evaluate.

    Returns:
        str: Strength rating ('Weak', 'Medium', 'Strong').
    """
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(not c.isalnum() for c in password)

    strength_score = sum([lower, upper, digit, special])

    if len(password) < 8 or strength_score < 3:
        return "Weak"
    elif len(password) < 12 or strength_score < 4:
        return "Medium"
    return "Strong"

def get_user_input(prompt, default=None, input_type=str):
    """Handles user input with optional defaults and type conversion.

    Args:
        prompt (str): The prompt to display to the user.
        default: The default value if no input is provided.
        input_type (type): The expected type of the input.

    Returns:
        The user's input converted to the specified type.

    Raises:
        ValueError: If input conversion fails.
    """
    while True:
        try:
            user_input = input(prompt + (f" [Default: {default}]" if default is not None else "") + ": ")
            if not user_input and default is not None:
                return default
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def yes_no_input(prompt, default="y"):
    """Prompts for a yes/no input with a default option.

    Args:
        prompt (str): The prompt to display to the user.
        default (str): The default value ('y' or 'n').

    Returns:
        bool: True for 'yes', False for 'no'.
    """
    default = default.lower()
    options = {"y": True, "n": False}

    while True:
        user_input = input(prompt + f" [y/n, Default: {default}]: ").strip().lower()
        if not user_input:
            return options[default]
        if user_input in options:
            return options[user_input]
        print("Invalid input. Please enter 'y' or 'n'.")

def main():
    print("\nWelcome to PyCipher!\n")

    try:
        # Get user preferences
        length = get_user_input("Enter password length", default=12, input_type=int)
        include_digits = yes_no_input("Include digits?", default="y")
        include_symbols = yes_no_input("Include symbols?", default="y")
        exclude_ambiguous = yes_no_input("Exclude ambiguous characters?", default="y")

        # Generate the password
        password = generate_password(
            length=length,
            include_digits=include_digits,
            include_symbols=include_symbols,
            exclude_ambiguous=exclude_ambiguous
        )

        # Display the password and its strength
        print("\nGenerated Password:", password)
        print("Password Strength:", check_password_strength(password))
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
