from django import forms 
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile
from django.utils import timezone
import random

class CategoryForm(forms.ModelForm):

    cats = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    name = forms.CharField(max_length=128,
                           help_text="Please enter the game name.")
    releasedate = forms.DateField(initial=timezone.now(), required=False,
                                  help_text="Release Date.")
    yturl = forms.CharField(max_length=128,
                            help_text="Please enter game video URL.")
    iosurl = forms.URLField(help_text="Please enter IOS App store download link.")
    andurl = forms.URLField(help_text="Please enter Google Play store download link.")
    pcurl = forms.URLField(help_text="Please enter PC download link.")

    introduction = forms.CharField(max_length=2048,
                                   help_text="Please enter introduction of the game.")
    review = forms.CharField(max_length=65536,
                             help_text="Please enter the review of the game.")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('cats', 'name', 'releasedate', 'yturl', 'iosurl', 'andurl', 'pcurl', 'introduction', 'review')


class PageForm(forms.ModelForm):

    message = forms.CharField(max_length=1024,
                              help_text="Please enter the comment for the game.")
    evaluation = forms.IntegerField(initial=0,
                                    help_text="Please enter your evaluation for the game.")
    commentdate = forms.DateField(initial=timezone.now(), required=False, help_text="Submition Date.")

    class Meta:
        model = Page
        exclude = ('category', 'username')


class UserForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User 
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=True)
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile 
        fields = ('age', 'website', 'picture')



