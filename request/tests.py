# from django.test import TestCase
# from django.test import RequestFactory, TestCase
# from .views import get_Request, RequestListView, all_requests
# from django.contrib.auth.models import User
from django.test import TestCase
from .forms import RequestForm
from .models import LOC_CHOICES, SUBJECTS
from django.utils import timezone

class RequestFormTests(TestCase):
    def test_forms(self):
        form_data = {'subject': 'something', 'location':'house', 'specific':'help'}
        form = RequestForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms2(self):
        form_data = {'subject': SUBJECTS[0][0], 'location':LOC_CHOICES[0][1], 'specific':'help'}
        form = RequestForm(data=form_data)
        self.assertTrue(form.is_valid)
    
    def test_forms3(self):
        form_data = {'subject': SUBJECTS[0][1], 'location':LOC_CHOICES[0][1]}
        form = RequestForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_forms4(self):
        form_data = {'subject': SUBJECTS[3][1], 'location':LOC_CHOICES[2][1], 'specific':'more help'}
        form = RequestForm(data=form_data)
        self.assertTrue(form.is_valid)
    
    def test_forms5(self):
        form_data = {'subject': SUBJECTS[0][1], 'location':LOC_CHOICES[0][1]}
        form = RequestForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_forms6(self):
        form_data = {'subject': SUBJECTS[6][1], 'location':'rice', 'specific':'cs is hard'}
        form = RequestForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms7(self):
        form_data = {'subject': SUBJECTS[6][1], 'location':LOC_CHOICES[0][1], 'specific':'cs is hard', 'date':'', 'author':''}
        form = RequestForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_forms8(self):
        form_data = {'subject': SUBJECTS[6][1], 'location':'rice', 'specific':'cs is hard', 'date':'', 'author':''}
        form = RequestForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms9(self):
        form_data = {'subject': SUBJECTS[6][1], 'location':LOC_CHOICES[0][1], 'specific':'cs is hard', 'date':timezone.now, 'author':''}
        form = RequestForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_forms10(self):
        form_data = {'subject': SUBJECTS[6][1], 'location':'rice', 'specific':'cs is hard', 'date':timezone.now, 'author':''}
        form = RequestForm(data=form_data)
        self.assertFalse(form.is_valid())    

# class RequestViewsTestCase(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='jacob', email='jacob@…', password='top_secret')

#     def test_get_request(self):
#         request = self.factory.get('')
#         request.user = self.user
#         response = get_Request(request)
#         self.assertEqual(response.status_code, 200)

#     def test_request_list(self):
#         request = self.factory.get('list/')
#         request.user = self.user
#         response = RequestListView.as_view()(request)
#         self.assertEqual(response.status_code, 200)
    
#     def test_all_requests(self):
#         request = self.factory.get('allrequests/')
#         request.user = self.user
#         response = all_requests(request)
#         self.assertEqual(response.status_code, 200)