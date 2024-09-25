import re
from flask import current_app

def validate_password(password):
    min_length = current_app.config['PASSWORD_MIN_LENGTH']

    if len(password) < min_length:
        return False, f"Password must more than {min_length} characters long"

    uppercase = re.search(r'[A-Z]', password)
    lowercase = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    categories = [uppercase, lowercase, digit, special_char]
    if sum(bool(cat) for cat in categories) < 2:
        return False, "Password must contain at least two categories of characters"

    return True, "Password is valid"
