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
    if (request.session['id']):
            request.session['name'] = None
            request.session['id'] = None
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
            request.session['id'] = user.id
            request.session['name'] = user.first_name
            return redirect('/')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)


def viewProduct(request, product_id):
    print(product_id)

    if(product_id == '1'):
        name = 'Veg Chow'
        image = "/static/register/images/chow.jpeg"
        print('chow')
    elif(product_id == '2'):
        name = 'Egg Roll'
        image = "/static/register/images/eggroll.jpg"
        print('roll')
    elif(product_id == '3'):
        name = 'Veg Burger'
        image = "/static/register/images/burger.jpeg"
        print('burger')
    elif(product_id == '4'):
        name = 'Pizza'
        image = "/static/register/images/pizza.jpeg"
        print('pizza')
    elif(product_id == '5'):
        name = 'Chicken Momo'
        image = "/static/register/images/momo.jpeg"
        print('momo')
    elif(product_id == '6'):
        name = 'Masala Dosa'
        image = "/static/register/images/dosa.jpg"
        print('dosa')

    data = {
        'name' : name,
        'image' : image
    }
    #return render(request, 'register/viewProduct.html')
    template = loader.get_template('register/viewProduct.html')
    return HttpResponse(template.render(data, request))
