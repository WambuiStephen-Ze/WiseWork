from django.contrib import admin

from .models import Log, Carousel, Section, Abote, About, Skills, Services, Contact, Call, Tramp, Testimony, Time, Team, \
    Features, Portfolio, Status, Client_status, Clients, Location, Contact_Us, Product, Reside, Omesa, Field, Header, Indicate, Main

# Register your models here.

admin.site.register(Log)

admin.site.register(Header)
admin.site.register(Reside)
admin.site.register(Omesa)
admin.site.register(Field)
admin.site.register(Indicate)

admin.site.register(Carousel)
admin.site.register(Section)

admin.site.register(Main)
# admin.site.register(Login)
# admin.site.register(Profile)
# admin.site.register(Logout)

admin.site.register(About)
admin.site.register(Abote)

admin.site.register(Contact_Us)
admin.site.register(Contact)

admin.site.register(Skills)
admin.site.register(Services)

admin.site.register(Call)

admin.site.register(Testimony)
admin.site.register(Tramp)

admin.site.register(Team)
admin.site.register(Time)

admin.site.register(Features)

admin.site.register(Portfolio)

admin.site.register(Status)

admin.site.register(Client_status)
admin.site.register(Clients)

admin.site.register(Location)

admin.site.register(Product)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'address')


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'rating')