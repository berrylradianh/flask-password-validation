import unittest
from app.routes import validate_password

class TestPasswordValidation(unittest.TestCase):
    def test_Fxmedia12345678(self):
        result, message = validate_password('Fxmedia12345678@')
        self.assertTrue(result)

    def test_AnotherSecurePwd(self):
        result, message = validate_password('AnotherSecurePwd$567')
        self.assertTrue(result)

    def test_SuperP(self):
        result, message = validate_password('SuperP@ssphrase123')
        self.assertTrue(result)

    def test_ShortPwd(self):
        result, message = validate_password('ShortPwd1!')
        self.assertFalse(result)
        self.assertEqual(message, "Password must be at least 15 characters long")

    def test_Password(self):
        result, message = validate_password('Password')
        self.assertFalse(result)
        self.assertEqual(message, "Password must be at least 15 characters long")

    def test_lowercaseonly(self):
        result, message = validate_password('lowercaseonly')
        self.assertFalse(result)

    def test_MISSINGUPPERANDSPECIAL(self):
        result, message = validate_password('MISSINGUPPERANDSPECIAL')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
