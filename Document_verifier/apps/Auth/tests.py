from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="gabriel", email="gabriel@test.com")
        User.objects.create(username="admin", email="gabriel1@test.com")

    def test_user_email_unique(self):
        u1 = User.objects.get(username="gabriel")
        u2 = User.objects.get(username="admin")
        self.assertNotEqual(u1.email, u2.email)
