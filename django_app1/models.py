from django.db import models
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    date=models.DateField(null=True)
    def __str__(self):
        return self.name
    

# #données choloate scraper
# class Result(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.CharField(max_length=255)
#     url = models.URLField()
    
class Company(models.Model):
    name = models.TextField(verbose_name="Name")
    #comment = models.TextField(verbose_name="Comment")
    sector = models.TextField( verbose_name="Sector")
    location = models.TextField(verbose_name="Location")
    url_posts = models.TextField( verbose_name="URL Posts")
    num_posts = models.TextField( verbose_name="Number of Posts")

    def __str__(self):
        return self.name
class Chaussure(models.Model):
    image_url = models.TextField(blank=True, null=True)
    #price est de type float
    price_cfa = models.FloatField(blank=True, null=True)
    product_url = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)