from flask import request, jsonify
import re
from app import app

def validate_password(password):
    if len(password) < 15:
        return False, "Password must be at least 15 characters long"

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
