from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from recipes.models import *
from recipes.forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

cats_bar = Category.objects.exclude(name__in=['Cuisines','Special Occasions']).order_by('name')

def index(request):
	#get all recipes, order alphabetically by name
	latest = Recipe.objects.order_by('-date_posted')[:6]
	#get all categories -- no order
	users = User.objects.order_by('-date_joined')[:6]

	top = Recipe.objects.order_by('cook_time')[:6]

	context_dict = {'latest':latest, 'users':users, 'top':top}
	response = render(request,'recipes/index.html', context=context_dict)
	return response

def about(request):
	#get users that are chefs -- order alphabetically by username
	chefs = Chef.objects.all()
	context_dict = {'chefs':chefs}

	response = render(request,'recipes/about.html', context=context_dict)
	return response

def faq(request):
	return render(request,'recipes/faq.html', {})

def trending(request):
	recipes = Category.objects.get(slug="st-patricks-day").recipe_set.all()
	return render(request,'recipes/trending.html', {'recipes':recipes})

def categories(request):
	#get all categories -- no order
	cats = Category.objects.all()
	context_dict = {'cats':cats}
	response = render(request,'recipes/categories.html', context=context_dict)
	return response

def register(request):
	registered = False
	if request.method=='POST':
		user_form = UserForm(data=request.POST)
		profile_form = ChefForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			if 'photo' in request.FILES:
				profile.photo = request.FILES['photo']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = ChefForm()
	return render(request, 'recipes/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		print(user)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print("Invalid ligin details: {0},{1}".format(username, password))
			return HttpResponseRedirect(reverse('invalidlogin'))
	else:
		return render(request, 'recipes/login.html', {})

def invalidlogin(request):
	return render(request,'recipes/invalidlogin.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

@login_required
def suggestion(request):
	form = SuggestForm()
	if request.method == 'POST':
		form = SuggestForm(data=request.POST)
		if form.is_valid():
			suggestion = form.save(commit=False)
			suggestion.author = request.user
			suggestion.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		print(form.errors)
	return render(request, 'recipes/suggestion.html', {'form':form})

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(data=request.POST)
		if form.is_valid():
			suggestion = form.save(commit=True)
			return HttpResponseRedirect(reverse('index'))
		else:
			print(form.errors)
	return render(request, 'recipes/contact.html', {'form':form})

@login_required
def addrecipe(request):
	form = AddRecipeForm(request.FILES)
	if request.method == 'POST':
		form = AddRecipeForm(request.POST, request.FILES)
		if form.is_valid():
			recipe = form.save(request.user.username)
			recipe.chef = request.user
			cats = form.cleaned_data.get('categories')
			if(len(cats) > 3):
				raise forms.ValidationError("You can't select more than 3 items.")
			else:
				recipe.save()
				for cat in cats:
					category = Category.objects.get(id=cat)
					recipe.categories.add(category)
			recipe.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			print(form.errors)
	return render(request, 'recipes/addrecipe.html', {'form':form})

def viewrecipe(request, recipe_name_slug):
	context_dict = {'cats_bar':cats_bar}
	try:
		recipe = Recipe.objects.get(slug=recipe_name_slug)
		reviews = Review.objects.filter(recipe=recipe).order_by("-date_posted")

		if len(reviews) > 0:
			avgRating = (Review.objects.filter(recipe=recipe).aggregate(Sum('rating'))["rating__sum"])/len(reviews)
			context_dict['avgRating'] = round(avgRating,2)
		else:
			context_dict['avgRating'] = "No rating yet."
		context_dict['recipe'] = recipe
		context_dict['reviews'] = reviews
	except:
		context_dict['recipe'] = None

	if request.user.is_authenticated():
		form = ReviewForm()
		if request.method == 'POST':
			form = ReviewForm(request.POST)
			if form.is_valid():
				review = form.save(commit=False)
				review.recipe = recipe
				review.author = request.user
				review.save()
				return redirect('/recipes/recipe/'+recipe_name_slug)
		else:
			print(form.errors)
		context_dict["form"] = form
	return render(request, 'recipes/recipe.html', context_dict)

def userprofile(request, username):
	context_dict = {}
	try:
		user = User.objects.get(username=username)
		chef = Chef.objects.get(user=user)
		recipes = Recipe.objects.filter(chef=user)
		reviews = Review.objects.filter(author=user)
		context_dict['reviews'] = reviews
		context_dict['recipes'] = recipes
		context_dict['chef'] = chef
	except:
		context_dict['chef'] = None

	return render(request, 'recipes/profile.html', context_dict)

@login_required
def edit_profile(request, username):
	if request.method == 'POST':
		edit = EditProfileForm(request.POST, request.FILES, instance=request.user)
		bio  = EditBioForm(request.POST, request.FILES, instance=request.user.chef)
		if edit.is_valid() and bio.is_valid():
			edit.save()
			bio.save()
			return redirect('/recipes/profile/'+username)
		else:
			print(edit.errors, bio.errors)
	else:
		edit = EditProfileForm(request.FILES, instance=request.user)
		bio = EditBioForm(request.FILES, instance=request.user.chef)

	context_dict = {'edit':edit,'bio':bio}
	return render(request, 'recipes/edit_profile.html', context_dict)

@login_required
def change_password(request, username):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('index')
		else:
			print("Passwords did not match.")
	else:
		form=PasswordChangeForm(data=request.POST, user=request.user)
	context_dict = {'form':form}

	return render(request, 'recipes/change_password.html', context_dict)

def show_category(request, cat_name_slug):
	context_dict = {}

	try:
		cat = Category.objects.get(slug=cat_name_slug)
		recipes = cat.recipe_set.all()
		subcats = Category.objects.filter(supercat=cat)
		context_dict['recipes'] = recipes
		context_dict['subcats'] = subcats
		context_dict['cat'] = cat
		context_dict['cats_bar'] = cats_bar
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['recipes'] = None

	return render(request, 'recipes/category.html', context_dict)
