from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.template import RequestContext
from LivinWater.forms import RegistrationForm, LoginForm
from lv_user.models import LVUser

def is_moder(func):
	def wrapper(request, *args, **kwargs):
		if request.user.is_authenticated() and request.user.is_staff:
			return func(request, *args, **kwargs)
		else:
			return HttpResponseRedirect("/auth")
	return wrapper

def index(request):
	return render_to_response('index.html', context_instance = RequestContext(request))
	
def registration(request):
	form = RegistrationForm()
	return render_to_response('registration.html', {'form': form}, context_instance = RequestContext(request))
	
def signup(request):
	username = request.POST['subject']
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	password = request.POST['password']
	confirm = request.POST['re_password']
	mail = request.POST['email']
	date_of_birth = request.POST['date_of_birth']
	form = RegistrationForm({'subject': username, 'password': password, 're_password': confirm, 'email': mail, 'date_of_birth': date_of_birth})
	if password==confirm:
		if form.is_valid():
			try:
				user = User.objects.get(username=username)
				form['subject'].className = 'short_test'
			except (User.DoesNotExist):
				user = User.objects.create_user(username=form.cleaned_data['subject'], email=form.cleaned_data['email'], password=password)
				user.is_staff = False
				user.save()
				return HttpResponseRedirect('/home')
	return render_to_response('registration.html', {'form': form}, context_instance = RequestContext(request))
	
def login(request):
	username = request.POST['subject']
	password = request.POST['password']
	form = LoginForm({'subject': username, 'password': password})
	if form.is_valid():
		user = auth.authenticate(username=form.cleaned_data['subject'], password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/home')
		else:
			return render_to_response('auth.html', context_instance = RequestContext(request))

def logout(request):
	if request.user.is_active:
		auth.logout(request)
	return HttpResponseRedirect("/home")

def authorization(request):
	form = LoginForm()
	return render_to_response('auth.html', {'form':form},context_instance = RequestContext(request))

def user_info(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/auth")
	try:
		lv_user = LVUser.objects.get(user=request.user)
	except (LVUser.DoesNotExist):
		lv_user = LVUser(user=request.user)
		lv_user.save()
	return render_to_response('user_info.html', {'lv_user':lv_user}, context_instance = RequestContext(request))
	
def user_edit(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/auth")
	return render_to_response('user_edit.html', context_instance = RequestContext(request))

@is_moder
def manage(request):
	return render_to_response('manage.html', context_instance = RequestContext(request))

@is_moder
def user_list(request):
	user_list = User.objects.all().order_by('-date_joined')
	return render_to_response('user_list.html', {'user_list': user_list}, context_instance = RequestContext(request))

@is_moder
def user_info_by_id(request, user_id):
	user_info = User.objects.get(pk=user_id)
	return render_to_response('user_id.html', {'user_info': user_info}, context_instance = RequestContext(request))
	
@is_moder
def groups_list(request):
	groups_list = Group.objects.all()
	return render_to_response('group_list.html', {'groups_list': groups_list}, context_instance = RequestContext(request))

@is_moder
def group_add(request):
	return render_to_response('group_add.html', context_instance = RequestContext(request))

@is_moder
def add_group(request):
	groupname = request.POST['groupname']
	group = Group(name=groupname)
	group.save()
	return HttpResponseRedirect("groups")