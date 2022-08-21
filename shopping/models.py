from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)
    slug = models.SlugField(unique = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField(upload_to='../static/product_images', blank=True)
    url = models.URLField(null = True)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField(upload_to='../static/product_images', blank=True)
    url = models.URLField(null = True)
    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=128)
    url = models.URLField()
    price = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    picture = models.ImageField(upload_to='../static/product_images', blank=True)
    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
