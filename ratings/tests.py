from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import HomePageView
from django.contrib.auth.models import User

# class LoginViewsTestCase(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='jacob', email='jacob@…', password='top_secret')

#     def test_homepage_get(self):
#         request = self.factory.get("")
#         request.user = self.user
#         response = HomePageView.as_view()(request)
#         self.assertEquals(response.status_code, 200)