from django.test import TestCase

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
        Profile.objects.create(user=user, major="meche", year="4")
        Profile.objects.create(user=user2, major="english", year="4")
        Profile.objects.create(user=user3, major="cs", year="1")
        Profile.objects.create(user=user4)

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
    
    def test_one_first_year_2(self):
        fys = Profile.objects.filter(year="1")
        self.assertTrue(len(fys)==1)
    
    def test_one_first_year_3(self):
        fys = Profile.objects.filter(year="1")
        self.assertTrue(len(fys)==1)
    
    def test_change_major(self):
        john = Profile.objects.get(major="meche")
        john.major = "cs"
        self.assertTrue(john.major=="cs")

    def test_change_major2(self):
        anna = Profile.objects.filter(major="english")
        anna.major="cs"
        self.assertTrue(anna.major=="cs")

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
        cs = User.objects.create_user(username="l33thaxor",
                                    email="luvhacking@cs.com",
                                    password="12345")
        cs2 = User.objects.create_user(username="badHacker",
                                    email="hatehacking@cs.com",
                                    password="12345")
        Profile.objects.create(user=cs, major="cs", year="1")
        Profile.objects.create(user=cs2, major="cs", year="1")
        cs_students = Profile.objects.filter(major="cs")
        self.assertEquals(len(cs_students), 3)
    
    def test_number_majors4(self):
        cs = User.objects.create_user(username="l33thaxor",
                                    email="luvhacking@cs.com",
                                    password="12345")
        cs2 = User.objects.create_user(username="badHacker",
                                    email="hatehacking@cs.com",
                                    password="12345")
        Profile.objects.create(user=cs, major="engl", year="1")
        Profile.objects.create(user=cs2, major="cs", year="1")
        cs_students = Profile.objects.filter(major="cs")
        self.assertEquals(len(cs_students), 2)    

