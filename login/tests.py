from django.test import TestCase

# Create your tests here.
from login.models import Profile
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        Profile.objects.create(user=user, major="meche", year="4")

    def test_animals_can_speak(self):
        """Major associated with profile is correctly"""
        kp = Profile.objects.get(major="meche")
        self.assertTrue(kp.year=="4")