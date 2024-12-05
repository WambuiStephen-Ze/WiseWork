from django.shortcuts import render

from . models import Log, Carousel, Section, Abote, About, Skills, Services,Contact, Call, Tramp, Testimony, Time, Team, Features, Portfolio, Status, Client_status, Clients, Location, Contact_Us, Product, Register, Login, Profile, Logout

from .serializers import logSerializer,CarouselSerializer, SectionSerializer, AboteSerializer, AboutSerializer, ServicesSerializer, ContactSerializer, CallSerializer, Contact_UsSerializer, TestimonySerializer, ProductSerializer, FeaturesSerializer, PortfolioSerializer, StatusSerializer, Client_statusSerializer, ClientsSerializer, LocationSerializer, TimeSerializer, TrampSerializer, TeamSerializer, SkillsSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer, LogoutSerializer

from rest_framework import viewsets


class LogView(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = logSerializer

class CarouselView(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class LoginView(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class LogoutView(viewsets.ModelViewSet):
    queryset = Logout.objects.all()
    serializer_class = LogoutSerializer


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


# class AboutUsView(viewsets.ModelViewSet):
#     queryset = About.objects.all()
#     serializer_class = About_UsSerializer


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
    logs = Log.objects.all()
    features = Features.objects.all()
    portfolios = Portfolio.objects.first()
    portfolio = Portfolio.objects.all()
    portfo = Portfolio.objects.all()
    status = Status.objects.all()
    customer_status = Client_status.objects.all()
    clients = Clients.objects.all()
    location = Location.objects.all()

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
        'logs': logs,
        'features': features,
        'portfolio': portfolio,
        'portfolios': portfolios,
        'portfo': portfo,

        'status': status,
        'customer_status': customer_status,
        'clients': clients,
        'location': location,
        'contacts': contacts,

    }

    return render(request, 'index.html', context )

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



def about(request):
    # abote = Abote.objects.first()
    # context = {
    #     'abote': abote,
    # }
    return render(request, 'about.html')

def contact(request):
    location = Location.objects.all()
    contacts = Contact.objects.first()
    context = {
        'location': location,
        'contacts': contacts,
    }
    return render(request, 'contact.html', context)

def services(request):
    skills = Skills.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'service-details.html', context)

def starters(request):
    return render(request, 'starter-page.html')
def portfolio(request):
    return render(request, 'portfolio-details.html')
def layout(request):
    logs = Log.objects.all()
    context = {
        'logs': logs,
    }
    return render(request, 'layout.html', context)

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
        return render(request, 'contact.html')


    return render(request,  'index.html')

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


def team(request):
    teams = Team.objects.all()
    team = Time.objects.first()
    context = {
        'teams': teams,
        'team': team,
    }

    return render(request, 'teams.html', context)


def register(request):
    registration = Register.objects.all()
    context = {
        'registration': registration,
    }

    return render(request, 'register.html', context)
def login(request):
    logins = Login.objects.all()
    context = {
        'logins': logins,

    }
    return render(request, 'login.html', context)

def logout(request):
    logouts = Logout.objects.all()
    context = {
        'logouts': logouts,

    }
    return render(request, 'login.html', context)