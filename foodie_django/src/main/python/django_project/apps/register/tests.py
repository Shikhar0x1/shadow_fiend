from django.test import TestCase
import models
from models import User
import views
from django.core.urlresolvers import reverse
import unittest
from selenium import webdriver


# models test
class RegisterTest(TestCase):

    def create_register(self, first_name="first", last_name="last", email="test@test.com", password="test"):
        return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)

    def test_register_creation(self):
        w = self.create_register()
        self.assertTrue(isinstance(w, User))
        self.assertEqual(w.__unicode__(), w.first_name)

# views (uses reverse)

    def test_register_homepage_view(self):
        w = self.create_register()
        url = reverse("apps.register.views.index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

##unittest
class TestLogin(unittest.TestCase):

    def create_register(self, first_name="Test", last_name="Test", email="test@test.com", password="test1234"):
        return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'/home/shikhar/geckodriver')

    def test_register_fire(self):
        self.driver.get("http://localhost:8000/loginPage")
        self.driver.find_element_by_id('fname').send_keys("Test")
        self.driver.find_element_by_id('lname').send_keys("Test")
        self.driver.find_element_by_id('r_email').send_keys("test@test.com")
        self.driver.find_element_by_id('r_password').send_keys("test1234")
        self.driver.find_element_by_id('r_cpassword').send_keys("test1234")
        self.driver.find_element_by_id('signup').click()
        self.assertIn("http://localhost:8000/loginPage", self.driver.current_url)

    def test_login_fire(self):
        self.driver.get("http://localhost:8000/loginPage")
        self.driver.find_element_by_id('email').send_keys("test@test.com")
        self.driver.find_element_by_id('password').send_keys("test1234")
        self.driver.find_element_by_id('submit').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def test_logout_fire(self):
        self.driver.get("http://localhost:8000/")
	print("Logout Successful")
        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
