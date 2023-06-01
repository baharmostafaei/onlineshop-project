from django.test import TestCase
from django.shortcuts import reverse
from .models import CustomUser
from django.contrib.auth import get_user_model

class AccountAppTests(TestCase):
    username = 'myusername'
    email = 'myusername@gmail.com'

    def setUp(self):
        self.credentials = {
            'username' : 'testuser',
            'password' : 'password'}
        CustomUser.objects.create_user(**self.credentials)
    
    def test_login(self):
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)


    def test_sign_up_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name= 'registration/signup.html')
    
    def test_sign_up_oage_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name= 'registration/signup.html')

    def test_sign_up_form(self):
        user = get_user_model().objects.create_user(
            self.username, 
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 2)
        self.assertEqual(get_user_model().objects.all()[1].username, self.username)
        self.assertEqual(get_user_model().objects.all()[1].email, self.email)



