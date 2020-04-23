# LOGIN TESTS
from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import display_login, display_profile, make_profile, update_profile

# Create your tests here.
from login.models import Profile
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        user2 = User.objects.create_user(username="anna", 
                                email="test@test.com",
                                password="password")
        user3 = User.objects.create_user(username="mark",
                                email="cs@uva.edu",
                                password="django")
        user4 = User.objects.create_user(username="undecided",
                                email="confused@test.com",
                                password="password")
        user5 = User.objects.create_user(username="louisa", 
                                email="le@virginia.edu", 
                                password="django")
        user6 = User.objects.create_user(username="alan", 
                                email="az@virginia.edu", 
                                password="django")
        user7 = User.objects.create_user(username="naresha", 
                                email="nn@virginia.edu", 
                                password="django")
        user8 = User.objects.create_user(username="ali", 
                                email="ac@virginia.edu", 
                                password="django")                                                      
        Profile.objects.create(user=user, major="meche", year="4")
        Profile.objects.create(user=user2, major="english", year="4")
        Profile.objects.create(user=user3, major="cs", year="1")
        Profile.objects.create(user=user4)
        Profile.objects.create(user=user5, major="")
        Profile.objects.create(user=user6, year="3")
        Profile.objects.create(user=user7, major="undecided")
        Profile.objects.create(user=user8)

    def test_animals_can_speak(self):
        """Major associated with profile is correctly"""
        kp = Profile.objects.get(major="meche")
        self.assertTrue(kp.year=="4")

    def test_multiple_fourth_years(self):
        fys = Profile.objects.filter(year="4")
        self.assertTrue(len(fys)==2)
    
    def test_one_first_year(self):
        fys = Profile.objects.filter(year="1")
        self.assertTrue(len(fys)==1)
    
    def test_one_third_year(self):
        tys = Profile.objects.filter(year="3")
        self.assertTrue(len(tys)==1)
    
    def test_one_undecided(self):
        und = Profile.objects.filter(major="undecided")
        self.assertTrue(len(und)==1)

    def test_change_major(self):
        john = Profile.objects.get(major="meche")
        john.major = "cs"
        self.assertTrue(john.major=="cs")

    def test_change_major2(self):
        anna = Profile.objects.filter(major="english")
        anna.major="cs"
        self.assertTrue(anna.major=="cs")
    
    def test_change_major3(self):
        anna = Profile.objects.filter(major="english")
        anna.major = "english"
        self.assertTrue(anna.major=="english")

    def test_change_major4(self):
        louisa = Profile.objects.filter(major="")
        louisa.major = "cs"
        self.assertTrue(louisa.major=="cs")
    
    def test_change_major5(self):
        alan = Profile.objects.get(year="3")
        alan.major = "cs"
        self.assertTrue(alan.major=="cs")

    def test_number_majors(self):
        cs = Profile.objects.filter(major="cs")
        self.assertTrue(len(cs)==1)

    def test_number_majors2(self):
        cs = User.objects.create_user(username="l33thaxor",
                                    email="luvhacking@cs.com",
                                    password="12345")
        Profile.objects.create(user=cs, major="cs", year="1")
        cs_students = Profile.objects.filter(major="cs")
        self.assertEquals(len(cs_students), 2)
    
    def test_number_majors3(self):
        meche = User.objects.create_user(username="mech",
                                        email="ilovemech@mech.com",
                                        password="mechanical")
        Profile.objects.create(user=meche, major="meche")
        meche_students = Profile.objects.filter(major="meche")
        self.assertEquals(len(meche_students), 2)
    
    def test_number_majors4(self):
        math = User.objects.create_user(username="math",
                                        email="math@math.com",
                                        password="fibonacci")
        Profile.objects.create(user=math, major="math")
        math_students = Profile.objects.filter(major="math")
        self.assertEquals(len(math_students), 1)
    
    def test_number_majors5(self):
        confused = User.objects.create_user(username="idk",
                                            email="unknown@idk.com",
                                            password="password")
        Profile.objects.create(user=confused, major="undecided", year="2")
        undecided_students = Profile.objects.filter(major="undecided")
        self.assertEquals(len(undecided_students), 2)                                    

    def test_change_year(self):
        john = Profile.objects.get(major="meche")
        john.year = "1"
        self.assertTrue(john.year=="1")

    def test_change_year2(self):
        anna = Profile.objects.filter(major="english")
        anna.year = "4"
        fys = Profile.objects.filter(year="4")
        self.assertTrue(len(fys), 3)
    
    def test_change_year3(self):
        anna = Profile.objects.filter(major="english")
        anna.year = "3"
        self.assertTrue(anna.year=="3")

    def test_change_year4(self):
        kp = Profile.objects.get(major="undecided")
        kp.year = "2"
        self.assertEquals(kp.year, "2")
    
    def test_change_year5(self):
        alan = Profile.objects.get(year="3")
        alan.year = "1"
        self.assertTrue(alan.year=="1")

# class LoginViewsTestCase(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='jacob', email='jacob@…', password='top_secret')

#     def test_login_display_get(self):
#         request = self.factory.get('/login')
#         request.user = self.user
#         response = display_login(request)
#         self.assertEqual(response.status_code, 200)
    
#     def test_login_display_post(self):
#         request = self.factory.post('/login')
#         request.user = self.user
#         response = display_login(request)
#         self.assertEqual(response.status_code, 200)
    
#     def test_profile_display_get(self):
#         request = self.factory.get('/profile')
#         request.user = self.user
#         response = display_profile(request)
#         self.assertEqual(response.status_code, 200)
    
#     def test_profile_display_post(self):
#         request = self.factory.post('/profile')
#         request.user = self.user
#         response = display_profile(request)
#         self.assertEqual(response.status_code, 200)
    
#     def test_make_profile_get(self):
#         request = self.factory.get('/profile')
#         request.user = self.user
#         response = make_profile(request)
#         self.assertEquals(response.status_code, 200)
    