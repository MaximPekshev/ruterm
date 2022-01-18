from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class ContactForm(forms.Form):
	
	contactName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
			'class': 'form-control input-box',
			'placeholder': 'Ваше Имя',
			'id': 'name',
            'name': 'name',
            'type': 'text'

		}))
	contactEmail = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={
			'class': 'form-control input-box',
			'placeholder': 'Ваш Email',
			'id': 'email',
            'name': 'email',
            'type': 'email'
		}))
	contactComment = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
			'class': 'form-control textarea-box',
			'placeholder': 'Сообщение',
			'id': 'message',
            'name': 'message',
			'rows': '8',
		}))
	captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)