from unittest import TestCase
import json
from .routes import app


class BaseTest(TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()


class TestRegister(BaseTest):
    def test_register(self):
        request = self.client.post('/auth/signup',
                                   content_type='application/json',
                                   data=json.dumps({"name": "charity", "username": "chacha",
                                                    "email": "chacha@gmail.com", "password": "1234",
                                                    "confirm_password": "1234"})
                                   )
        response = json.loads(request.data)
        self.assertEqual(request.status_code, 201)
        self.assertEqual(response["message"],
                         "successfully registered as chacha")
