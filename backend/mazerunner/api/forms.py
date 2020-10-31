"""
Class containing all HTML forms
"""

from django import forms
from users.models import User

class signupForm(forms.Form):
	email = forms.EmailField(label="Email")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(signupForm, self).clean()
		email = cleaned_data["email"]
		password = cleaned_data["password"]
		confirm_password = cleaned_data["confirm_password"]

		is_same = password == confirm_password
		is_exists = User.objects.filter(email=email).exists()

		if is_exists:
			raise forms.ValidationError(
				"Account already exists"
			)
		if not is_same:
			raise forms.ValidationError(
				"Passwords do not match"
			)
		