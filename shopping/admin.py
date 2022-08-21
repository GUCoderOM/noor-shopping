from django.contrib import admin
from django.contrib.auth.models import User
from shopping.models import UserProfile, Category, Product,SubCategory



class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user',)}
    #list_display = ('username', 'email', 'age')

admin.site.register(UserProfile,UserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SubCategory)
