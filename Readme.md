# Password Validation in Node.js

## About

This is a simple password validation program built using **Flask** that validates passwords based on specific criteria. The validation ensures that:

- Privileged account passwords must be at least **15 characters** long.
- Passwords must include characters from at least **two (2) of the following categories**:
  - Uppercase (A-Z)
  - Lowercase (a-z)
  - Digits (0-9)
  - Special Characters (!, @, #, $, %, etc.)

Also, create unit tests for each of the following passwords:
  - Fxmedia12345678@
  - AnotherSecurePwd$567
  - SuperP@ssphrase123
  - ShortPwd1!
  - Password
  - lowercaseonly
  - MISSINGUPPERANDSPECIAL

If the password doesn't meet these criteria, an error is thrown with an appropriate message. Unit tests are provided to validate the functionality.

## Requirements

- Python (version >= 3.8)
- Flask

## Installation

Follow these steps to install and run the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/berrylradianh/flask-password-validation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-password-validation
   ```

3. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a .env.json file based on the env.example.json file (if needed):

   ```bash
   cp env.example.json .env.json
   ```

6. Start the Flask server:
    ```bash
        flask run
    ```

7. Open your browser and navigate to http://127.0.0.1:5000/validate_password to test the password validation functionality.

# Testing

To run the tests, execute the following command:

```bash
python -m unittest discover -s test
```

## License

This project is licensed under the MIT License.
