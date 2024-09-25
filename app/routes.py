from flask import request, jsonify, current_app
import re
from app import app

def validate_password(password):
    min_length = current_app.config['PASSWORD_MIN_LENGTH']
    max_length = current_app.config['PASSWORD_MAX_LENGTH']

    if len(password) < min_length or len(password) > max_length:
        return False, f"Password must be between {min_length} and {max_length} characters long"

    uppercase = re.search(r'[A-Z]', password)
    lowercase = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    categories = [uppercase, lowercase, digit, special_char]
    if sum(bool(cat) for cat in categories) < 2:
        return False, "Password must contain at least two categories of characters"

    return True, "Password is valid"

@app.route('/validate_password', methods=['POST'])
def validate():
    password = request.json.get('password')
    is_valid, message = validate_password(password)
    return jsonify({"valid": is_valid, "message": message})
