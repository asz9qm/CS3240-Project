from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import charge, HomePageView
from login.models import Profile
from django.contrib.auth.models import User


# class PaymentViewsTestCase(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='jacob', email='jacob@…', password='top_secret')
    
#     def charge_view_test(self):
#         # tbd
#         self.assertEquals(1, 1)

    
        

