from django import forms

class addTopic(forms.Form):
	title = forms.CharField(initial='Заголовок')
	text = forms.CharField(initial='Текст')