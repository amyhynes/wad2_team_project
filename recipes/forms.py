from django import forms
from recipes.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','password')

# our version of UserProfile
class ChefForm(forms.ModelForm):
	photo = forms.ImageField(required=False)
	bio = forms.Textarea()
	class Meta:
		model = Chef
		fields = ('photo','bio')

#asks for title of rating, actual rating 0-5 decimal, and any additional comments
class ReviewForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(),max_length=128, label="Title")
	rating = forms.DecimalField(widget=forms.NumberInput(), min_value=0, max_value=5, required=True, label="Rating 1 to 5")
	comment = forms.CharField(widget=forms.Textarea(),label="Any additional comments")

	class Meta:
		model = Review
		exclude = ('recipe','author','date_posted')

class SuggestForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(), label="Leave a suggestion for a new cuisine or occasion!", required=False)

	class Meta:
		model = Suggestion
		fields = ('comment',)

class ContactForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(), label="First name", required=True)
	last_name = forms.CharField(widget=forms.TextInput(), label="Last name", required=True)
	email = forms.CharField(widget=forms.EmailInput(), label="Email address", required=True)
	comment = forms.CharField(widget=forms.Textarea(), help_text="Leave your comment or question here.", required=True)

	class Meta:
		model = Contact
		fields = ('first_name','last_name','email', 'comment')

#asls for name of recipe, a photo, and cook time of recipe
class AddRecipeForm(forms.ModelForm):
	CATEGORIES =(
		("1","Breakfast"),
		("2","Lunch"),
		("3","Dinner"),
		("4","Dessert"),
		("6","Italian"),
		("7","American"),
		("8","Mexican"),
		("9","Chinese"),
		("10","Indian"),
		("11","Japanese"),
		("13","St Patrick's Day"),
		("14","Easter"),
		("15","Christmas"),
		("16","Halloween"),
		("17","4th of July"),
		("18","Valentine's Day"),
	)
	name = forms.CharField(widget=forms.TextInput(), help_text="Give your recipe a name", required=True)
	photo = forms.ImageField(required=True)
	cook_time = forms.IntegerField(min_value=0, initial=0, help_text="in minutes", required=True)
	about = forms.CharField(widget=forms.Textarea(), label="Description", required=True)
	ingredients = forms.CharField(widget=forms.Textarea(), label=" Ingredients", required=True)
	steps = forms.CharField(widget=forms.Textarea(), label="Steps", required=True)
	#slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	categories = forms.MultipleChoiceField(widget=forms.SelectMultiple(),choices=CATEGORIES, required=True, help_text="Hold down Control (Command on Mac) to choose up to three!")

	class Meta:
		model = Recipe
		fields = ('name','photo','cook_time','categories','about','ingredients','steps')

	def save(self, username):
		author = User.objects.get(username=username)
		self.chef = author
		print(self.cleaned_data)
		recipe = super(AddRecipeForm, self).save(commit=False)
		return recipe;

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('email','first_name','last_name',)

	def clean_password(self):
		return ""

class EditBioForm(UserChangeForm):
	class Meta:
		model = Chef
		fields = ('photo', 'bio')

	def clean_password(self):
		return ""
