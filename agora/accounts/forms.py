from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms

class UserCustomChangeForm(UserChangeForm):
    class Meta:
       model = get_user_model()
       fields = ('user_name', 'job', 'profilepic', 'text')


class UserCustomCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS, label='생년월일 | yyyymmdd',)

    username = forms.CharField(label='아이디')

    text = forms.Textarea()

    class Meta:
       model = get_user_model()

       fields = ('username',
                 'user_name',
                 'gender',
                 'email',
                 'profilepic',
                 'job',
                 'age',
                 'text',
                 'date_of_birth')

