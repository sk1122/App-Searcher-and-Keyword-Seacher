from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from .models import GooglePlayModel, AppleAppModel
from .forms import GooglePlayStore, AppleAppStore

c = Client()


class GoogleTestCase(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user('zoidberg')
        self.entry = GooglePlayModel(user=user, name="com.android.chrome", app_name="Google Chrome: Fast & Secure", image="https://lh3.googleusercontent.com/KwUBNPbMTk9jDXYS2AeX3illtVRTkrKVh5xR1Mg4WHd0CG2tV4mrh1z3kXi5z_warlk=s180", developer="Google LLC",
                                     description="Google Chrome is a fast, easy to use, and secure web browser. Designed for Android, Chrome brings you personalized news articles, quick links to your favorite sites, downloads, and Google Search and G...", downloads="5,000,000,000+", reviews="19,858,126", ratings="4.4")

    def test_init(self):
        GooglePlayStore({'app_id': "com.android.chrome"})

    def test_init_without_entry(self):
        if self.assertRaises(KeyError):
            GooglePlayStore()


class GoogleFormTest(TestCase):
    def test_forms(self):
        form = GooglePlayStore()
        self.assertEqual(form.fields["app_id"].label, "Enter App")

    def test_googleform_valid(self):
        form = GooglePlayStore(data={
            'app_id': 'com.android.chrome'
        })

        # self.assertFieldOutput(
        #     TextInput, {'com.android.chrome': 'com.android.chrome'})

        self.assertTrue(form.is_valid())


class AppleFormTest(TestCase):

    def test_form_name(self):
        form = AppleAppStore()
        self.assertEqual(form.fields["app_name"].label, "App Name")

    def test_form_id(self):
        form = AppleAppStore()
        self.assertEqual(form.fields["app_id"].label, "App Id")

    def test_appleform_valid(self):
        form = AppleAppStore(data={
            'app_name': 'google chrome',
            'app_id': '5354123541'
        })

        self.assertTrue(form.is_valid())


class ViewsTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = c.get('/app/')
        # Page Redirects to Login Page
        self.assertEqual(response.status_code, 302)

    def test_url(self):
        response = c.get('/')
        # Page Redirects to Login Page
        self.assertEqual(response.status_code, 302)


class AuthenticationTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testing',
            'password': 'test@password'
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # login
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now, fails however
        self.assertTrue(response.context['user'].is_active)


# class MySeleniumTests(StaticLiveServerTestCase):
#     fixtures = ['user-data.json']

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(10)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     def test_login(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
#         username_input = self.selenium.find_element_by_name("username")
#         username_input.send_keys('sk1122')
#         password_input = self.selenium.find_element_by_name("password")
#         password_input.send_keys('jiokiojio')
#         self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

class AjaxTest(TestCase):

    def test_ajax(self):
        response = c.post('/app/ajax/', {"app_id": "com.android.chrome"},
                          **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 302) # Redirect Happens
