import unittest
from main import app, session
from model.user_model import UserModel

class TestSignUp(unittest.TestCase) :
    def setUp(self):
        self.test_app = app.test_client()
    
    def test_success_signup(self):
        response = self.test_app.post("/signup", json={
            "username": "user2",
            "password": "pw2",
            "name": "name2",
            "email": "2@naver.com"
                }
            )
        self.assertEqual(201, response.status_code)
        user = session.query(UserModel).filter(UserModel.username == "user2", UserModel.password == 'pw2',
        UserModel.name == 'name2', UserModel.email == '2@naver.com')
        self.assertIsNotNone(user)


unittest.main()
    
