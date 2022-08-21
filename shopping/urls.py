from django.urls import path
from shopping import views

app_name = 'shopping'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('about/',views.about, name = 'about'),
    path('grocery/',views.grocery, name = 'grocery'),
    path('category/<category>',views.category, name='category'),
    path('subcategory/<subcategory>',views.subcategory, name='subcategory'),
    path('product/<product>',views.product, name='product'),

]
