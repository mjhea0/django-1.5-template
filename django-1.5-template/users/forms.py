from django import forms
from django.utils.translation import ugettext_lazy as _

from users.models import User

class RegistrationForm(forms.ModelForm):
	password_match = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-block-level', 'placeholder': _('Password (again)')}, render_value=True))

	class Meta:
		model = User
		fields = ('username', 'password', 'email')
		widgets = {
			'username':			forms.TextInput		(attrs={'class': 'input-block-level', 'placeholder': _('Username')}),
			'password':			forms.PasswordInput	(attrs={'class': 'input-block-level', 'placeholder': _('Password')}, render_value=True),
			'email':			forms.TextInput		(attrs={'class': 'input-block-level', 'placeholder': _('Email')}),
		}

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()

		password = cleaned_data.get('password')
		password_match = cleaned_data.get('password_match')

		if password != password_match:
			self._errors['password'] = self.error_class(_("Passwords don't match."))

		return cleaned_data