from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import mail
from login.models import Profile
from django.contrib.auth.models import User

# class EmailViewsTestCase(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='jacob', email='jacob@…', password='top_secret')

#     def test_mail_display_get(self):
#         request = self.factory.get('')
#         request.user = self.user
#         response = mail(request)
#         self.assertEqual(response.status_code, 200)
    
#     def test_mail_display_post(self):
#         request = self.factory.post('')
#         request.user = self.user
#         response = mail(request)
#         self.assertEqual(response.status_code, 200)

