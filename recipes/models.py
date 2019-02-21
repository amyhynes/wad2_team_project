from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    TYPES = (
        ('CAT', 'Category'),
        ('SUB', 'Subcategory')
    )
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=25, choices=TYPES, default='CAT')
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    supercat = models.ForeignKey('self', null=True, related_name='category')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Chef(models.Model):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    email = models.CharField(max_length=50)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='profile_pics', default='profile_pics/anon.png')

    def __str__(self):
        return self.username

class Recipe(models.Model):
    chef = models.ForeignKey(Chef)
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=128, unique=True)
    photo = models.ImageField(upload_to='food_pics', blank=True)
    cook_time = models.IntegerField(default=0)

    def __str__(self):
        return self.name
