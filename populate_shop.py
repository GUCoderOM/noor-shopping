import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'noor.settings')

import django
django.setup()

from shopping.models import Category, Product,SubCategory
def populate():
    #c = add_cat(cat)
    #
    # First, we will create lists of dictionaries containing the Products
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    breakfastspreads_Products = [
    {"name": "Nutella Hazelnut Spread With Cocoa 400g",
    "url":"http://127.0.0.1:8000/shopping/grocery/breakfast-&-spreads/nutella-hazelnut-spread-with-cocoa-400g",
    "price": 0.4,
    "picture":"../../static/product_pictures/n.jpg"},
    {"name":"Alpen Strawberry & Yoghurt Cereal Bar 29g",
    "url":"http://127.0.0.1:8000/shopping/grocery/Breakfast-&-Spreads/alpen-strawberry-&-yoghurt-cereal-bar-29g",
    "price": 2.45,
    "picture":"../../static/product_pictures/strawberry.jpg"},
    {
    "name":"Bread",
    "url":"http://127.0.0.1:8000/shopping/grocery/breakfast-&-spreads/bread",
    "price":0.100,
    "picture":"../../static/product_pictures/bread.jpg",
    },{
    "name":"cheese",
    "url":"http://127.0.0.1:8000/shopping/grocery/breakfast-&-spreads/cheese",
    "price":0.750,
    "picture":"../../static/product_pictures/cheese.jpg",
    },{
    "name":"Cheese Spread",
    "url":"http://127.0.0.1:8000/shopping/grocery/breakfast-&-spreads/cheese",
    "price":1.250,
    "picture":"../../static/product_pictures/spread_cheese.jpg",
    },{
    "name":"Butter",
    "url":"http://127.0.0.1:8000/shopping/grocery/breakfast-&-spreads/butter",
    "price":0.650,
    "picture":"../../static/product_pictures/butter.jpg",
    },]

    beverage_Products = [
    {"name": "Actiph Alkaline Ionised Water 600ml",
     "url": "http://127.0.0.1:8000/shopping/grocery/beverage/actiph-alkaline-ionised-water-600ml",
     "price": 1.8,
     "picture":"../../static/product_pictures/awater.jpg"},
     {"name": "Oasis Water 1 Gallon",
     "url" :"http://127.0.0.1:8000/shopping/grocery/beverage/oasis-water-1-gallon",
     "price": 1,
     "picture":"../../static/product_pictures/water.jpg"
     },
     {
     "name":"Pepsi",
     "url":"http://127.0.0.1:8000/shopping/grocery/beverage/pepsi",
     "price":0.150,
     "picture":"../../static/product_pictures/pepsi.jpg",
     },{
     "name":"Cola",
     "url":"http://127.0.0.1:8000/shopping/grocery/beverage/cola",
     "price":0.150,
     "picture":"../../static/product_pictures/cola.jpg",
     },{
     "name":"Schweppes",
     "url":"http://127.0.0.1:8000/shopping/grocery/beverage/schweppes",
     "price":5.490,
     "picture":"../../static/product_pictures/schweppes.jpg",
     },{
     "name":"Sprite",
     "url":"http://127.0.0.1:8000/shopping/grocery/beverage/sprite",
     "price":0.150,
     "picture":"../../static/product_pictures/sprite.jpg",
     },]
    chipssnacks_Products = [{
    "name":"Pringles Original Chips XXL 200g",
    "url": "http://127.0.0.1:8000/shopping/grocery/chipssnacks/pringles-original-chips-xxl-200g",
    "price": 2.3,
    "picture":"../../static/product_pictures/pringles.jpg",},

    {"name": "Al Mudhish Tortilla Chips Pizza Flavour 200g",
    "url":"http://127.0.0.1:8000/shopping/grocery/chipssnacks/al-mudhish-tortilla-chips-pizza-flavour-200g",
    "price":0.7,
    "picture":"../../static/product_pictures/tortilla.jpg"},
    {
    "name":"Gingerbread Men",
    "url":"http://127.0.0.1:8000/shopping/grocery/chipssnacks/ginger-bread-men",
    "price":3.000,
    "picture":"../../static/product_pictures/ginger.jpg",
    },{
    "name":"Pretzels",
    "url":"http://127.0.0.1:8000/shopping/grocery/chipssnacks/pretzels",
    "price":0.800,
    "picture":"../../static/product_pictures/pretzel.jpg",
    },{
    "name":"Cookies",
    "url":"http://127.0.0.1:8000/shopping/grocery/chipssnacks/cookies",
    "price":5.490,
    "picture":"../../static/product_pictures/cookie.jpg",
    },
    ]

    dentalhealthcare_Products = [{
    "name": "Listerine",
    "url": "http://127.0.0.1:8000/shopping/grocery/dentalhealthcare/listerine",
    "price": 1.8,
    "picture":"../../static/product_pictures/listerine.jpg",
    },{
    "name":"Sensodyne Toothbrush",
    "url":"http://127.0.0.1:8000/shopping/grocery/dentalhealthcare/sensodyne-toothbrush",
    "price": 1.370,
    "picture":"../../static/product_pictures/sensodyne.jpg"
    },{
    "name":"Colgate",
    "url":"http://127.0.0.1:8000/shopping/grocery/dentalhealthcare/colgate",
    "price":0.500,
    "picture":"../../static/product_pictures/colgate.jpg"
    },{
    "name":"Electric Toothbrush",
    "url":"http://127.0.0.1:8000/shopping/grocery/dentalhealthcare/electric-toothbrush",
    "price":20.500,
    "picture":"../../static/product_pictures/Electric.jpg"
    },{
    "name":"Floss Mint Waxed",
    "url":"http://127.0.0.1:8000/shopping/grocery/dentalhealthcare/floss",
    "price":1.370,
    "picture":"../../static/product_pictures/floss.jpg"
    },{
    "name":"Strawberry Toothpaste",
    "url":"http://127.0.0.1:8000/shopping/grocery/dentalhealthcare/strawberry-toothpaste",
    "price":1.370,
    "picture":"../../static/product_pictures/strawberrytooth.jpg"
    },
    ]

    cats = {"Grocery" : {"Breakfast & Spreads": breakfastspreads_Products,
    "Beverage": beverage_Products, "Chips & Snacks": chipssnacks_Products,"Dental & Healthcare":dentalhealthcare_Products},
    "Fresh Food": {},"Electronics":{},"Home & Living":{}}

    cat_pics = {"Grocery":"../../static/images/grocery.jpg",
    "Fresh Food": "../../static/images/fresh.jpg",
    "Electronics":"../../static/images/electronics.jpg",
    "Home & Living":"../../static/images/homeliving.jpg"}
    cat_url = {"Grocery":"../../shopping/grocery",
    "Fresh Food": "../../shopping/fresh",
    "Electronics":"../../shopping/electronics",
    "Home & Living":"../../shopping/homeliving"}

    subcat_pics = {"Beverage": "../../static/images/beverage.jpg",
    "Breakfast & Spreads": "../../static/images/breakfast.jpg",
    "Chips & Snacks": "../../static/images/snacks.jpg",
    "Dental & Healthcare":"../../static/images/dental.jpg",
    "Skincare": "../../static/images/skincare.jpg",
    "Chocolate": "../../static/images/chocolate.jpg"}

    subcat_url = {"Beverage": "../../shopping/beverage.jpg",
    "Breakfast & Spreads": "../../shopping/breakfast.jpg",
    "Chips & Snacks": "../../shopping/snacks.jpg",
    "Dental & Healthcare":"../../shopping/dental.jpg",
    "Skincare": "../../shopping/skincare.jpg",
    "Chocolate": "../../shopping/chocolate.jpg"}
    cats = dict(cats)
    for cat in cats.keys():
        c = add_cat(cat)
        subs = cats[cat]
        for sub_cat in cats[cat].keys():
            sub = add_sub(sub_cat,c)
            for p in cats[cat][sub_cat]:
                add_Product(c,sub, p["name"], p["url"],p["price"],p["picture"])
        for p in Product.objects.filter(category=c):
            print("- {0} - {1} - {2}".format(str(p.category), str(p.subcategory), str(p)))
# Print out the categories we have added.
    for cat in cat_url.keys():
        add_Cat_Image(cat, cat_pics[cat])
        add_Cat_Url(cat,cat_url[cat])
        print("Added image and URL to cat", cat)
    for p in Product.objects.filter(category=c):
        print("- {0} - {1} - {2}".format(str(p.category), str(p.subcategory), str(p)))
    for subcat in subcat_url.keys():
        add_Subcat_Image(subcat, subcat_pics[subcat])
        add_Subcat_Url(subcat,subcat_url[subcat])
        print("Added image and URL to subcat", subcat)


def add_Product(cat,sub, name, url,price,picture):
    p = Product.objects.get_or_create(category = cat, name=name)[0]
    p.category = cat
    p.subcategory = sub
    p.url=url
    p.price=price
    p.picture=picture
    p.save()
    return p
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c
def add_sub(subcat,cat):
    sub = SubCategory.objects.get_or_create(name=subcat)[0]
    sub.category = cat
    sub.save()
    return sub
def add_Subcat_Image(subcat, picture):
    sub = SubCategory.objects.get_or_create(name=subcat)[0]
    sub.picture = picture
    sub.save()
    return sub
def add_Subcat_Url(subcat,url):
    sub = SubCategory.objects.get_or_create(name=subcat)[0]
    sub.url = url
    sub.save()
def add_Cat_Url(cat,url):
    c = Category.objects.get_or_create(name=cat)[0]
    c.url = url
    c.save()
    return c
def add_Cat_Image(cat, picture):
    c = Category.objects.get_or_create(name=cat)[0]
    c.picture = picture
    c.save()
    return c
# Start execution here!
if __name__ == '__main__':
    print("Starting Shopping population script...")
    populate()
