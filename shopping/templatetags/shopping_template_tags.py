from django import template
from django.contrib.auth.models import User
from shopping.models import UserProfile
from django.template.defaultfilters import stringfilter

register = template.Library()
