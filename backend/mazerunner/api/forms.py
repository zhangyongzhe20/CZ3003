"""
Class containing all HTML forms
"""
from django.contrib.auth import get_user_model
from django import forms


class signupForm(forms.Form):
    is_admin = forms.BooleanField(label="I am a Teacher", required=False)
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Password", help_text="Required for Teachers only", widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput, required=False)

    def clean(self):
        cleaned_data = super(signupForm, self).clean()
        password = cleaned_data["password"]
        is_admin = cleaned_data["is_admin"]
        confirm_password = cleaned_data["confirm_password"]
        email = cleaned_data["email"]
        # add restriction for registration
        if not (email.endswith('@e.ntu.edu.sg') or email.endswith('@ntu.edu.sg')):
            raise forms.ValidationError('Only NTU email addresses are accepted!')
        try:
            teacher = get_user_model().objects.get(email = email)
        except:
            pass
        raise forms.ValidationError('This email address is already registered!')
        
        is_none = password == ''
        is_same = password == confirm_password

        if is_admin and is_none:
            raise forms.ValidationError(
                "Please create a password"
            )
        elif not is_none and not is_same:
            raise forms.ValidationError(
                "Passwords do not match"
            )
        
