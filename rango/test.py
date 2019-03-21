from django.test import TestCase
from rango.models import Category
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import Client
from django.contrib.staticfiles import finders
from django.core.urlresolvers import reverse

User = get_user_model()
# Create your tests here.

class CategoryTests(TestCase):
    def test_ensure_classify_are_not_empty(self):
        cat = Category(name=' ')
        cat.save()
        self.assertEqual((cat.name != ''), True)

class IndexViewTests(TestCase):
    def test_index_view_when_login(self):
       
        response = self.client.get(reverse('index')) 
        self.assertEqual(response.status_code, 200) 
        self.assertQuerysetEqual(response.context['categories'], [])

class IndexLoginTests(TestCase):
    def test_index_view_when_not_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "register")
        self.assertContains(response, "login")
        

class LoginTests(TestCase):
    def test_user_log_in(self):
        user = User.objects.create(username='helloaa')
        user.set_password('123456asdfgh')
        user.save()
        c = Client()
        login = c.login(username='helloaa', password='123456asdfgh')
        self.assertTrue(login)

class ModelTests(TestCase):

    def setUp(self):
        try:
            from population_script import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')
            
    def get_category(self, name):
        
        from rango.models import Category
        try:                  
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:    
            cat = None
        return cat

    def test_python_cat_with_likes(self):
        cat = self.get_category('Minecraft')
        self.assertEquals(cat.likes, 6)

    def test_admin_interface_page_view(self):
        from rango.admin import PageAdmin
        self.assertIn('category', PageAdmin.list_display)

    def test_does_slug_field_work(self):
        from rango.models import Category
        cat = Category(name='how do i create a slug in django')
        cat.save()
        self.assertEqual(cat.slug,'how-do-i-create-a-slug-in-django')


class GeneralTests(TestCase):
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('img/core-img/logo.png')
        self.assertIsNotNone(result)


class formViewTests(TestCase):

    def form_test_data(self):
        from rango.forms import CategoryForm
        form = CategoryForm(data={'name': "aa", 'introduction': "mp"})
        self.assertTrue(form.is_valid())
