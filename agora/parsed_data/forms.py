from django import forms
from .models import Pg_Board, Pg_Comment, Pg_Comment2, Pg_Board2, Pa_Board, Pa_Board2, Pa_Comment, Pa_Comment2, Par_Board, Par_Board2, Par_Comment, Par_Comment2  # Model Form 을 사용하기 위해 import 한다.

class Pg_BoardForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
                'class': 'content-type',
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
            }
        )
    )
    file = forms.FileField(
        label='파일선택',
        help_text='최대크기 42메가바이트'
    )
    class Meta:
        model = Pg_Board
        fields = ['title', 'content',]

class Pg_CommentForm(forms.ModelForm):
    class Meta:
        model = Pg_Comment
        fields = ['content',]


class Pg_BoardForm2(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
                'class': 'content-type',
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
            }
        )
    )
    file = forms.FileField(
        label='파일선택',
        help_text='최대크기 42메가바이트'
    )
    class Meta:
        model = Pg_Board2
        fields = ['title', 'content',]

class Pg_CommentForm2(forms.ModelForm):
    class Meta:
        model = Pg_Comment2
        fields = ['content',]

############################################################################################
############################################ PA ############################################
############################################################################################

class Pa_BoardForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
                'class': 'content-type',
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
            }
        )
    )
    file = forms.FileField(
        label='파일선택',
        help_text='최대크기 42메가바이트'
    )
    class Meta:
        model = Pa_Board
        fields = ['title', 'content',]

class Pa_CommentForm(forms.ModelForm):
    class Meta:
        model = Pa_Comment
        fields = ['content',]


class Pa_BoardForm2(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
                'class': 'content-type',
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
            }
        )
    )
    file = forms.FileField(
        label='파일선택',
        help_text='최대크기 42메가바이트'
    )
    class Meta:
        model = Pa_Board2
        fields = ['title', 'content',]

class Pa_CommentForm2(forms.ModelForm):
    class Meta:
        model = Pa_Comment2
        fields = ['content',]

############################################################################################
############################################ PAR ############################################
############################################################################################


class Par_BoardForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
                'class': 'content-type',
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
            }
        )
    )
    file = forms.FileField(
        label='파일선택',
        help_text='최대크기 42메가바이트'
    )
    class Meta:
        model = Par_Board
        fields = ['title', 'content',]

class Par_CommentForm(forms.ModelForm):
    class Meta:
        model = Par_Comment
        fields = ['content',]


class Par_BoardForm2(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
                'class': 'content-type',
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
            }
        )
    )
    file = forms.FileField(
        label='파일선택',
        help_text='최대크기 42메가바이트'
    )
    class Meta:
        model = Par_Board2
        fields = ['title', 'content',]

class Par_CommentForm2(forms.ModelForm):
    class Meta:
        model = Par_Comment2
        fields = ['content',]
