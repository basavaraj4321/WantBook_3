# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from signin.forms import RegistrationForm, EidtProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import registrationForm,signinForm

# Create your views here.

def home(request):
	return render(request , 'home.html')

def signin1(request):

	if request.method == 'POST':
		loginForm = signinForm(request.POST)
		if loginForm.is_valid():
			user = loginForm.cleaned_data['username']
			try:
				formUser = User.objects.get(username = user).username
			except :
				return loadNewForm(request)
			print(user,formUser)
			if formUser == user:
				return render(request, 'signin/loginform/home.html')
			else:
				return loadNewForm(request)
	else:
		return loadNewForm(request)

def loadNewForm(request):
	regForm = registrationForm()
	loginForm = signinForm()
	context = {
		"loginForm":loginForm,
		"regForm":regForm
	}
	return render(request, 'signin/loginform/login.html', context)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/home/')
	else:
		form = RegistrationForm()
		args = {'form' : form}
		return render(request, 'signin/loginform/register.html',args)

@login_required
def profile(request):
		args = {'user' : request.user}
		return render(request, 'signin/loginform/profile.html',args)

def edit_profile(request):
	if request.method == 'POST':
		form = EidtProfileForm(request.POST,instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('/account/home/')
	else:
		form = EidtProfileForm(instance	 = request.user)
		args = {'form' : form}
		return render(request, 'signin/loginform/edit_profile.html',args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST,user = request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/home/')
	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form' : form}
		return render(request, 'signin/loginform/change_password.html',args)
