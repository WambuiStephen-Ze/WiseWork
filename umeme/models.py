from django.db import models

# from umeme.views import residential


# logo medel

class Log(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="log")

    def __str__(self):
        return self.title

class Main(models.Model):
    name = models.CharField(max_length=100, default='image')

    image = models.ImageField(upload_to='images/', default='image')

    def __str__(self):
        return self.name





# carousel models

class Carousel(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


# carousel section model

class Section(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# about models

class About(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    desc1 = models.TextField()
    desc2 = models.TextField()
    desc3 = models.TextField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

# clients model
class Abote(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# clients models
class Clients(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name




# clients status models

class Client_status(models.Model):
    number = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', default=None)

    def __str__(self):
        return self.title



# features models

class Features(models.Model):
    name = models.CharField(max_length=50)
    desc=models.TextField()

    def __str__(self):
        return self.name


# services models
class Skills(models.Model):
    title = models.CharField(max_length=50)
    desc=models.CharField(max_length=50)

class Services(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/', default= 'none')

    def __str__(self):
        return self.title

    # services models

# services header
class Header(models.Model):
    title = models.CharField(max_length=50)
    desc=models.TextField()

# residential
class Reside(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/', default='none')

    def __str__(self):
        return self.title


# industrial
class Indicate(models.Model):
        title = models.CharField(max_length=50)
        desc = models.TextField()
        image = models.ImageField(upload_to='images/', default='none')

        def __str__(self):
            return self.title

# commercial
class Omesa(models.Model):

    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/', default='none')

    def __str__(self):
        return self.title
# fieldwork
class Field(models.Model):
        title = models.CharField(max_length=50)
        desc = models.TextField()
        image = models.ImageField(upload_to='images/', default='none')

        def __str__(self):
            return self.title


# call to action models

class Call(models.Model):
    button = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title



# portfolio models

# class Folio(models.Model):
#     title = models.CharField(max_length=50)
#     desc=models.CharField(max_length=50)

class Portfolio(models.Model):
    slide = models.CharField(max_length=50, default="")
    slide1 = models.CharField(max_length=50, default="")
    head = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name



# happy client models

class Status(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/', default= 'none')

    def __str__(self):
        return self.title

# testimonial models

class Testimony(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Tramp(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title



# teams models
class Team(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default= 'none')

    def __str__(self):
        return self.name
class Time(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()

class Location(models.Model):
    icon_choices  = [
        ('bi-geo-alt', 'Location'),
        ('bi-telephone', 'Contact'),
        ('bi-envelope', 'Email'),
    ]
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title




class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.CharField(max_length=50, default='0')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='images/', )
    label1 = models.CharField(max_length=50, default='0')
    label2 = models.CharField(max_length=50, default='0')
    label3 = models.CharField(max_length=50, default='0')
    desc1 = models.TextField(default='')
    desc2 = models.TextField(default='')
    desc3 = models.TextField(default='')

    def __str__(self):
        return self.name

