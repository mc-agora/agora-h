from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms

class UserCustomChangeForm(UserChangeForm):
    class Meta:
       model = get_user_model()
       fields = ('email', 'first_name', 'last_name')

class UserCustomCreationForm(UserCreationForm):
    birthdate = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS)
    class Meta:
       model = get_user_model()

       fields = ('user_id','username','birthdate','gender','email','job','profilepic','age')

