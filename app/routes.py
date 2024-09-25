from flask import request, jsonify
from app import app
from utils.validators import validate_password

@app.route('/validate_password', methods=['POST'])
def validate():
    password = request.json.get('password')
    is_valid, message = validate_password(password)
    return jsonify({"valid": is_valid, "message": message})
