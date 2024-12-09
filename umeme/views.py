from django.shortcuts import render, redirect
from .models import (Log, Carousel, Reside, Omesa, Field, Header, Section, Abote, About, Skills, Services,
                     Contact, Call, Tramp, Testimony, Time, Team, Features, Portfolio, Status, Client_status, Clients,
                     Location, Contact_Us, Product, Indicate, Main)

from .serializers import (logSerializer,CarouselSerializer, SectionSerializer, AboteSerializer, AboutSerializer, ServicesSerializer, ContactSerializer, CallSerializer, Contact_UsSerializer, TestimonySerializer, ProductSerializer, FeaturesSerializer, PortfolioSerializer, StatusSerializer, Client_statusSerializer, ClientsSerializer, LocationSerializer, TimeSerializer, TrampSerializer, TeamSerializer, SkillsSerializer)
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . credentials import AccessToken, Password
import requests



class LogView(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = logSerializer

class CarouselView(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class SectionView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class AboteView(viewsets.ModelViewSet):
    queryset = Abote.objects.all()
    serializer_class = AboteSerializer


class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ServicesView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CallView(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer


class Contact_UsView(viewsets.ModelViewSet):
    queryset = Contact_Us.objects.all()
    serializer_class = Contact_UsSerializer



class TestimonyView(viewsets.ModelViewSet):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FeaturesView(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer


class PortfolioView(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class Client_statusView(viewsets.ModelViewSet):
    queryset = Client_status.objects.all()
    serializer_class = Client_statusSerializer


class ClientsView(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TimeView(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TrampView(viewsets.ModelViewSet):
    queryset = Tramp.objects.all()
    serializer_class = TestimonySerializer


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SkillsView(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


# @login_required(login_url='login')
def index(request):
    carousels = Carousel.objects.all()
    teams = Team.objects.all()
    team = Time.objects.first()

    skills = Skills.objects.first()
    services = Services.objects.all()
    calls = Call.objects.all()

    abote = Abote.objects.first()
    about = About.objects.all()

    contact = Contact_Us.objects.all()
    contacts = Contact.objects.first()

    testimony = Testimony.objects.all()
    tramp = Tramp.objects.first()

    sections = Section.objects.all()
    # logs = Log.objects.all()
    features = Features.objects.all()
    portfolios = Portfolio.objects.first()
    portfolio = Portfolio.objects.all()
    portfo = Portfolio.objects.all()
    status = Status.objects.all()
    customer_status = Client_status.objects.all()
    clients = Clients.objects.all()
    location = Location.objects.all()
    images = Main.objects.all()

    context = {
        'carousel': carousels,
        'teams': teams,
        'team': team,
        'skills' : skills,
        'services': services,
        'calls': calls,
        'about': about,
        'abote': abote,
        'contact': contact,
        'testimony': testimony,
        'tramps': tramp,
        'sections': sections,
        # 'logs': logs,
        'features': features,
        'portfolio': portfolio,
        'portfolios': portfolios,
        'portfo': portfo,
        'images' : images,

        'status': status,
        'customer_status': customer_status,
        'clients': clients,
        'location': location,
        'contacts': contacts,

    }

    return render(request, 'index.html', context )


@login_required(login_url='login')
def insert(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        image = request.POST['image']

        carousels = carousel(
            name=name,
            title=title,
            image=image
        )
        carousels.save()


@login_required(login_url='login')
def about(request):
    about = About.objects.all()
    context = {
        'about': about,
    }

    return render(request, 'about.html', context)


@login_required(login_url='login')
def contact(request):
    location = Location.objects.all()
    contacts = Contact.objects.first()
    context = {
        'location': location,
        'contacts': contacts,
    }
    return render(request, 'contact.html', context)


@login_required(login_url='login')
def services(request):
    skills = Skills.objects.all()
    services = Services.objects.all()
    context = {
        'skills': skills,
        'services' : services,
    }
    return render(request, 'service-details.html', context)

@login_required(login_url='login')
def starters(request):
    return render(request, 'starter-page.html')

@login_required(login_url='login')
def portfolio(request):
    images = Main.objects.all()

    return render(request, 'portfolio-details.html', {'images': images})

# @login_required(login_url='login')
# def layout(request):
#     logs = Log.objects.all()
#     context = {
#         'logs': logs,
#     }
#     return render(request, 'layout.html', context)

@login_required(login_url='login')
def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact_Us(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()
        messages.success(request, 'Message sent successfully')

        return redirect('/contact/')



    return render(request,  'index.html')


@login_required(login_url='login')
def team(request):
    teams = Team.objects.all()
    team = Time.objects.first()
    context = {
        'teams': teams,
        'team': team,
    }

    return render(request, 'teams.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        return JsonResponse({'message': message})
    return JsonResponse({'error' : 'Invalid request'}, status=400)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password incorrect!')
            return redirect('login')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')



def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exist')
                return redirect('registerUser')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect('registerUser')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name

        )
        user.save()

        return redirect('login')
    else:
        messages.info(request, 'Please fill all the fields correctly')
        return render(request, 'register.html')
@login_required(login_url='login')
def stkpush(request):
    return render(request, 'sktpush.html')

@login_required(login_url='login')
def pay(request):
    if request.method == 'POST':
        phone = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        access_token =AccessToken.access_token
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        header = {'Authorization': "Bearer %s" % access_token}

        request = {

            "BusinessShortCode": Password.shortcode,
            "Password": Password.decoded_password,
            "Timestamp": Password.timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": Password.shortcode,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",
            "AccountReference": "WiseWork",
            "TransactionDesc": "Bought Products"

        }
        print(request)
        response = requests.post(api_url, json=request, headers=header)
        print(response)
        return HttpResponse('Success')

@login_required(login_url='login')
def cart(request):

    return render(request, 'cart.html')


@login_required(login_url='login')
def checkout(request):

    return render(request, 'checkout.html')
def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']

# def insert(request):
#     profile = Profile.objects.first()
#     if request.method == 'POST':
#         if 'save' in request.POST:
@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    rating_range = range(1, 6)
    context = {
        'products': products,
        'rating_range': rating_range

    }
    for product in products:
        product.full_stars = int(product.rating)  # Number of full stars
        product.half_star = product.rating % 1 >= 0.5  # True if a half-star is needed
        product.empty_stars = 5 - product.full_stars - (1 if product.half_star else 0)

    return render(request, 'product.html', context)


def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        #geting new values
        prod_name = request.POST["prod_name"]
        prod_price = request.POST["prod_price"]
        prod_qty = request.POST["prod_qty"]
        prod_category = request.POST["prod_category"]
        prod_desc = request.POST["prod_desc"]
        prod_img = request.FILES["prod_img"]

        #equating the new values to the existing product
        product.prod_name = prod_name
        product.prod_price = prod_price
        product.prod_qty = prod_qty
        product.prod_category = prod_category
        product.prod_desc = prod_desc
        product.prod_img = prod_img

        #saving product
        product.save()

        #Re direct to homepage
        return redirect("products:insert")

    return render(request, "update_product.html", {"product": product})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("update_product")


# passing the user input into the model

def insert_data(request):
    if request.method == "POST":
        prod_name = request.POST["prod_name"]
        prod_price = request.POST["prod_price"]
        prod_qty = request.POST["prod_qty"]
        prod_category = request.POST["prod_category"]
        prod_desc = request.POST["prod_desc"]
        prod_img = request.FILES["prod_img"]


        product = Product(prod_name=prod_name,
                          prod_price=prod_price,
                          prod_qty=prod_qty,
                          prod_category=prod_category,
                          prod_desc=prod_desc,
                          prod_img=prod_img
                          )
        # to save the variable
        product.save()
        return redirect('fetch')




    return render(request, "insert.html")


def header(request):
    skills = Header.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, "service-details.html", context)
def residential(request):
    services = Reside.objects.all()
    context = {
        'services': services,

    }
    return render(request, 'residential.html', context)
def industrial(request):
    indst_items = Indicate.objects.all()
    context = {
         'indst_items': indst_items,

    }
    return render(request, 'industrial.html', context)
def fieldwork(request):
    portfo = Field.objects.all()
    context = {

        'portfo': portfo,
    }
    return render(request, 'fieldwork.html', context)
def commercial(request):
    portfolio = Omesa.objects.all()

    context = {
        'portfolio': portfolio,
    }
    return render(request, 'commercial.html', context)
# def fetch(request):
#     products = Product.objects.all()
#     return render(request, 'fetch.html', {"products": products} )