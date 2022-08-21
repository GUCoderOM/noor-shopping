from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from shopping.models import User,UserProfile,Category,SubCategory,Product
from shopping.forms import UserForm,UserProfileForm
from django.views.generic.list import ListView
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from shopping.models import *
# Create your views here.

def index(request):
    cat = Category.objects.all()
    return render(request, 'shopping/index.html',context = {"cat":cat})
def about(request):
    return render(request, 'shopping/about.html', context = {})
def grocery(request):
    sub = SubCategory.objects.all()
    return render(request, 'shopping/grocery.html', context = {'sub':sub})

def category(request, category):
    cat = Category.objects.filter(name = category)[0]
    sub = SubCategory.objects.filter(category__name__startswith = category)
    return render(request, 'shopping/category.html', context = {"cat":cat,'sub':sub})
def subcategory(request,subcategory):
    sub = SubCategory.objects.filter(name = subcategory)[0]
    products = Product.objects.filter(subcategory__name__startswith = subcategory)
    return render(request, 'shopping/subcategory.html', context = {'sub':sub,'products':products})
def product(request,product):
    p = Product.objects.filter(name = product)[0]
    return render(request, 'shopping/product.html', context = {'p':p})
