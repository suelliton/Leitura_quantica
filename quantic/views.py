# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .forms import UsuarioCadastroForm, UsuarioLoginForm, UsuarioEditForm
from django.http import HttpResponseRedirect
from .models import User
import requests

#views

def register_user(request):
	if request.method == 'GET':
		form_cadastro_user = UsuarioCadastroForm()
		form_login_user = UsuarioLoginForm()
		return render(request,"quantic/register_user.html",{'form_cadastro_user':form_cadastro_user,'form_login_user':form_login_user})
	else:#post
		form = UsuarioCadastroForm(request.POST)
    	if form.is_valid():
			user = form.save(commit = False)
			if user.password == request.POST['rpassword']:
				new_user = User()
				new_user.password = user.password
				new_user.name = user.name
				new_user.login = user.login
				new_user.email = user.email

				users_login = User.objects.filter(login = new_user.login)
				users_email = User.objects.filter(email = new_user.email)
				form_cadastro_user = UsuarioCadastroForm()
				form_login_user = UsuarioLoginForm()

				if len(users_login) > 0: # se tiver retornado uma lista maior que 0 ja tem login cadastrado
					menssage = "Já existe um usuário cadastrado com  esse login "
					return render(request,"quantic/register_user.html",{'form_cadastro_user':form_cadastro_user,'form_login_user':form_login_user,'menssage':menssage})
				elif len(users_email) > 0: # se tiver retornado uma lista maior que 0 ja tem email cadastrado
					menssage = "Já existe um usuário cadastrado com esse email "
					return render(request,"quantic/register_user.html",{'form_cadastro_user':form_cadastro_user,'form_login_user':form_login_user,'menssage':menssage})
				else:
					new_user.save()
					#enviaEmail(novo_usuario)
					email = new_user.email;
					return render(request,"quantic/confirm_register.html",{'email':email})
			else:
				menssage = "Senhas não coincidem"
				return render(request,"quantic/login.html",{'form_cadastro_user':form_cadastro_user,'form_login_user':form_login_user,'menssage':menssage})


def login(request):
	if request.method == "GET":
		if request.session.get('id_logged'):
	       		return HttpResponseRedirect("index")
	    	else:
	       		form_login_user = UsuarioLoginForm()
	       		return render(request,"quantic/login.html",{'form_login_user':form_login_user})

	else:   #se  for post
		form_login_user = UsuarioLoginForm(request.POST)
		if form_login_user.is_valid():
			users = User.objects.all()
			for user in users:
				if user.login == request.POST['login'] and user.password == request.POST['password']:
					request.session['id_logged'] = user.id
					request.session['login_logged'] = user.login
					return HttpResponseRedirect('index')
			message = 'User not found'
			return render(request,"quantic/login.html",{'form_login_user':form_login_user,'message':message})

def logout(request):
    try:
        del request.session['id_logged']
        del request.session['login_logged']
    except KeyError:
        pass
    return HttpResponseRedirect("http://localhost:8000/")


def user(request):
	if request.session.get('id_logged'):
		id_logged = request.session.get('id_logged')
		login_logged = request.session.get('login_logged')
		return render(request,"quantic/user.html",{'id_logged':id_logged,'login_logged':login_logged})
	return HttpResponseRedirect('login')


def index(request):
	if request.session.get('id_logged'):
		id_logged = request.session.get('id_logged')
		login_logged = request.session.get('login_logged')
		return render(request,"quantic/index.html",{'id_logged':id_logged,'login_logged':login_logged})
	return HttpResponseRedirect('login')

def edit_user(request):
	if request.session.get('id_logged'):# se tiver usuario logado
		id_search = request.session.get('id_logged')
		user = get_object_or_404(User, pk=id_search)
		if request.method == "GET":
			form_edit_user = UsuarioEditForm(instance=user)
			return render(request, 'quantic/edit_user.html', {'form_edit_user':form_edit_user})
		else:#se fpr Post
			form_edit_user = UsuarioEditForm(request.POST, instance=user)
        	if form_edit_user.is_valid():
            		post_edit_user = form.save(commit=False)
            		post_edit_user.save()
			return render(request,"quantic/home.html",{})







def home(request):
	return render(request,"quantic/home.html",{})

#functions
