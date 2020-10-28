from django import forms

class CreateUsersForm(forms.Form):

    login = forms.CharField(widget=forms.TextInput, label='Введите имя')
    email = forms.CharField(widget=forms.TextInput, label='Эл. почта')
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')
    conf_password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')

class LoginUseForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput, label='Эл. почта')
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')