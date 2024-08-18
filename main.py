import string
import secrets
import random

def generate_password(length=12, include_digits=True, include_symbols=True, exclude_ambiguous=True):
    """Generates a random password based on given parameters.

    Args:
        length (int, optional): Password length. Defaults to 12.
        include_digits (bool, optional): Include digits. Defaults to True.
        include_symbols (bool, optional): Include symbols. Defaults to True.
        exclude_ambiguous (bool, optional): Exclude ambiguous characters. Defaults to True.

    Returns:
        str: Generated password.
    """

    if length <= 0:
        raise ValueError("Password length must be positive.")

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if exclude_ambiguous:
        ambiguous_chars = 'l1IiL0Oo'
        characters = ''.join(c for c in characters if c not in ambiguous_chars)

    return ''.join(secrets.choice(characters) for _ in range(length))

def check_password_strength(password):
    """Checks password strength based on basic criteria.

    Args:
        password (str): The password to check.

    Returns:
        str: Strength level (weak, medium, strong).
    """
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(not c.isalnum() for c in password)

    if sum([lower, upper, digit, special]) < 3:
        return "weak"
    elif sum([lower, upper, digit, special]) < 4:
        return "medium"
    else:
        return "strong"

def get_yes_no_input(prompt, default_value="y"):
  """Gets yes/no input from the user with error handling.

  Args:
      prompt (str): The prompt to display to the user.
      default_value (str, optional): The default value to assume if no input is provided. Defaults to "y".

  Returns:
      bool: True if the user enters "y" (or the default value), False otherwise.
  """
  while True:
    user_input = input(prompt + " ") or default_value
    if user_input.lower() in ("y", "n"):
      return user_input.lower() == "y"
    else:
      print("Error: Invalid input. Please enter 'y' or 'n'.")

def main():
  try:
    length = int(input("Enter password length (default 12): ") or 12)

    include_digits = get_yes_no_input("Include digits? (y/n, default y): ")
    include_symbols = get_yes_no_input("Include symbols? (y/n, default y): ")
    exclude_ambiguous = get_yes_no_input("Exclude ambiguous chars? (y/n, default y): ")

    password = generate_password(
        length=length,
        include_digits=include_digits,
        include_symbols=include_symbols,
        exclude_ambiguous=exclude_ambiguous,
    )

    print("Generated Password:", password)
    print("Password Strength:", check_password_strength(password))
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
