from django import forms

class RegistrationForm(forms.Form):
	subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'short_test'}))
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	
	date_of_birth = forms.DateField(required=False)
	skype = forms.CharField(required=False)
	city = forms.CharField(required=False)
	country = forms.CharField(required=False)

	password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'short_test'}))
	re_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'short_test'}))
	
	email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class':'short_test'}))
	date_of_birth = forms.CharField()
	
	def clean_subject(self):
		subject = self.cleaned_data['subject']
		num_words = len(subject)
		if num_words < 3:
			raise forms.ValidationError("Некорректный логин")
		return subject

class LoginForm(forms.Form):
	subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'short_test'}))
	password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'short_test'}))

	def clean_subject(self):
		subject = self.cleaned_data['subject']
		num_words = len(subject)
		if num_words < 3:
			raise forms.ValidationError("Некорректный логин")
		return subject