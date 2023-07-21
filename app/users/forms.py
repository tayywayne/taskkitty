from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(),
    )


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(),
    )
    password_confirm = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(),
    )
