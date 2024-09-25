import re
from flask import current_app

def validate_password(password):
    """
    Validate the password according to the following rules:
    - Password must be between min_length and max_length (from .env.json).
    - Password must include characters from at least two of the following categories:
        - Uppercase (A-Z)
        - Lowercase (a-z)
        - Digits (0-9)
        - Special characters (!, @, #, $, etc.)
    """
    min_length = current_app.config['PASSWORD_MIN_LENGTH']
    max_length = current_app.config['PASSWORD_MAX_LENGTH']

    # Check the length of the password
    if len(password) < min_length or len(password) > max_length:
        return False, f"Password must be between {min_length} and {max_length} characters long"

    # Check for character categories
    uppercase = re.search(r'[A-Z]', password)
    lowercase = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Ensure password contains characters from at least two categories
    categories = [uppercase, lowercase, digit, special_char]
    if sum(bool(cat) for cat in categories) < 2:
        return False, "Password must contain at least two categories of characters"

    return True, "Password is valid"
