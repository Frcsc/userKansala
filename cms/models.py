from django.db import models
from django.urls import reverse

# Create your models here.

class VISIBILITY(models.TextChoices):
    SHOW_ON_HOME_PAGE = ("SHOW_ON_HOME_PAGE", "Show_on_home_page")
    DO_NOT_SHOW_ON_HOME_PAGE = ("DO_NOT_SHOW_ON_HOME_PAGE", "Do_not_show_on_home_page")

class PropertyListModel(models.Model):

    image = models.ImageField(upload_to="property-list/images/")
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    price = models.IntegerField()
    show_on_home_page = models.CharField(max_length=512, choices=VISIBILITY.choices, default=VISIBILITY.DO_NOT_SHOW_ON_HOME_PAGE)
    number_of_bedrooms = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Property Listings"
    
    def get_absolute_url(self):
        return reverse('properties', args=[str(self.id)])


class PeopleModel(models.Model):
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    image = models.ImageField(upload_to="people/images/")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "People"


