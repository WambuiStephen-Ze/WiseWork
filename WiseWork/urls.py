"""
URL configuration for WiseWork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from umeme.views import LogView, CarouselView, SectionView, AboteView, AboutView, ServicesView, ContactView, CallView, Contact_UsView, TestimonyView, ProductView, FeaturesView, PortfolioView, StatusView, Client_statusView, ClientsView, LocationView, TimeView, TrampView, TeamView, SkillsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('log', LogView)
router.register('carousel', CarouselView)
router.register('section', SectionView)
router.register('abote', AboteView)
router.register('about', AboutView)
router.register('services', ServicesView)
router.register('contact', ContactView)
router.register('call', CallView)
router.register('contact', Contact_UsView)
# router.register('about-detail', AboutUsView)
router.register('testimony', TestimonyView)
router.register('product', ProductView)
router.register('features', FeaturesView)
router.register('portfolio', PortfolioView)
router.register('status', StatusView)
router.register('client_status', Client_statusView)
router.register('clients', ClientsView)
router.register('location', LocationView)
router.register('teams', TimeView)
router.register('tramp', TrampView)
router.register('team', TeamView)
router.register('skills', SkillsView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('', include ('umeme.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
