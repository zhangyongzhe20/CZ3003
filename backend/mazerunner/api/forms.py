"""
Class containing all HTML forms
"""

from django import forms

class signupForm(forms.Form):
	is_admin = forms.BooleanField(label="I am a Teacher", required=False)
	email = forms.EmailField(label="Email")
	password = forms.CharField(label="Password", help_text="Required for Teachers only", widget=forms.PasswordInput, required=False)
	confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, required=False)

	def clean(self):
		cleaned_data = super(signupForm, self).clean()
		password = cleaned_data["password"]
		is_admin = cleaned_data["is_admin"]
		confirm_password = cleaned_data["confirm_password"]

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
		