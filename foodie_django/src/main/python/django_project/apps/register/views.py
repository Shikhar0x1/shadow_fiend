from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.contrib import messages
import bcrypt
from models import User

def index(request):
    return render(request, 'register/home.html')

def loginPage(request):
    return render(request, 'register/index.html')

def logout(request):
    #if (request.session['id']):
    request.session['name'] = None
    return redirect('/')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/loginPage')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            #request.session['id'] = user.id
            request.session['name'] = user.first_name
            return redirect('/')
    return redirect('/')


def viewProduct(request, product_id):

    if(product_id == '1'):
        name = 'Veg Chow'
        image = "/static/register/images/chow.jpeg"
        restaurant = 'Volga Restaurant'
        address = 'azara, Azara'
        price = 'Rs. 190'
        offersZ = 'Use ORDERIT to get 50% off on Zomato'
        offersS = '20% off on Swiggy'
        offerU = 'No offer'
        url = 'https://www.swiggy.com/guwahati/volga-restaurant-azara-azara'
        print('chow')
    elif(product_id == '2'):
        name = 'Egg Roll'
        image = "/static/register/images/eggroll.jpg"
        restaurant = 'Volga Restaurant'
        address = 'azara, Azara'
        price = 'Rs. 70'
        offersZ = 'No offer'
        offersS = '20% off on Swiggy'
        offerU = 'No offer'
        url = 'https://www.swiggy.com/guwahati/volga-restaurant-azara-azara'
        print('roll')
    elif(product_id == '3'):
        name = 'Veg Burger'
        image = "/static/register/images/burger.jpeg"
        restaurant = 'Meat & Eat'
        address = 'Azara, Azara'
        price = 'Rs. 75'
        offersZ = 'No offer'
        offersS = '15% off on Swiggy'
        offerU = 'No offers'
        url = 'https://www.swiggy.com/guwahati/meat-eat-azara-maligaon'
        print('burger')
    elif(product_id == '4'):
        name = 'Pizza'
        image = "/static/register/images/pizza.jpeg"
        restaurant = 'Lazeez Pizza'
        address = 'azara, Azara'
        price = 'Rs. 190'
        offersZ = 'No offer'
        offersS = 'No offer'
        offerU = 'No offer'
        url = 'https://www.swiggy.com/guwahati/lazeez-pizza-vip-chowk-azara'
        print('pizza')
    elif(product_id == '5'):
        name = 'Chicken Momo'
        image = "/static/register/images/momo.jpeg"
        restaurant = 'Taste Of Heaven'
        address = 'Maligaon, Azara'
        price = 'Rs. 90'
        offersZ = 'No offer'
        offersS = 'No offer'
        offerU = 'No offers'
        url = 'https://www.swiggy.com/guwahati/lazeez-pizza-vip-chowk-azara'
        print('momo')
    elif(product_id == '6'):
        name = 'Masala Dosa'
        image = "/static/register/images/dosa.jpg"
        restaurant = 'Kamakhya Grand Chat House'
        address = 'Azara, Azara'
        price = 'Rs. 100'
        offersZ = 'No offers'
        offersS = '15% off on Swiggy'
        offerU = 'No offers'
        url = 'https://www.swiggy.com/guwahati/kamakhya-grand-chat-house-azara-azara'
        print('dosa')

    data = {
        'name' : name,
        'image' : image,
        'restaurant' : restaurant,
        'address' : address,
        'price' : price,
        'offerZ' : offersZ,
        'offersS' : offersS,
        'offerU' : offerU,
        'url' : url
    }
    #return render(request, 'register/viewProduct.html')
    template = loader.get_template('register/viewProduct.html')
    return HttpResponse(template.render(data, request))
