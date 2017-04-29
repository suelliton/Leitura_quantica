from django import forms
from .models import User


class UsuarioCadastroForm(forms.ModelForm):
	rpassword = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ('name','email','login','password','rpassword')
class UsuarioLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('login','password')
class UsuarioEditForm(forms.ModelForm):
	rpassword = forms.CharField(max_length = 20)
	class Meta:
		model = User
		#fields = ('image_upload','name','email','login','password','rpassword','image')
		fields = ('name','email','login','password','rpassword')
