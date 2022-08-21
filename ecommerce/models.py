from django.db import models

class Shoppy(models.Model):
    icon        = models.ImageField(upload_to="shoppy/")
    title       = models.CharField(max_length=50)
    description = models.TextField()
    phone       = models.CharField(max_length=20)
    address     = models.CharField(max_length=200)
    fb_link     = models.URLField(blank=True, null=True)
    tw_link     = models.URLField(blank=True, null=True)
    ins_link    = models.URLField(blank=True, null=True)
    li_link     = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

class Slider(models.Model):
    image = models.ImageField(upload_to="slider/")
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.title
        
class Offer(models.Model):
    title = models.CharField(max_length=250)
    rate = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="offer/")
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="product/")
    price = models.IntegerField(default=0)
    discound = models.IntegerField(default=0)
    price_after_discount = property(lambda self: self.price - (self.price * self.discound / 100))
    def __str__(self):
        return self.title

class About_Company(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    icon_name = models.CharField(max_length=50)
    def __str__(self):
        return self.title
