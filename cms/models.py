from django.db import models
from django.urls import reverse

# Create your models here.


class VISIBILITY(models.TextChoices):
    SHOW_ON_HOME_PAGE = ("SHOW_ON_HOME_PAGE", "Show_on_home_page")
    DO_NOT_SHOW_ON_HOME_PAGE = ("DO_NOT_SHOW_ON_HOME_PAGE", "Do_not_show_on_home_page")


class PropertyType(models.TextChoices):
    APARTMENT = ("Apartment", "Apartment")
    SHOP = ("Shop", "Shop")
    OFFICE_SPACE = ("Office_Space", "Office_Space")
    HOUSE = ("House", "House")


class TypeOfOffer(models.TextChoices):
    BUY = ("Buy", "Buy")
    RENT = ("Rent", "Rent")

class PropertyListModel(models.Model):
    image = models.ImageField(upload_to="property-list/images/")
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    floor_size = models.DecimalField(
        max_digits=548, decimal_places=2, blank=True, null=True
    )
    psf = models.DecimalField(max_digits=548, decimal_places=2, blank=True, null=True)
    price = models.IntegerField()
    number_of_bathroom = models.IntegerField(blank=True, null=True)
    type_of_property = models.CharField(
        max_length=512, choices=PropertyType.choices, default=PropertyType.APARTMENT
    )
    show_on_home_page = models.CharField(
        max_length=512,
        choices=VISIBILITY.choices,
        default=VISIBILITY.DO_NOT_SHOW_ON_HOME_PAGE,
    )
    number_of_bedrooms = models.CharField(max_length=64, null=True, blank=True)
    type_of_offer = models.CharField(
        max_length=512, choices=TypeOfOffer.choices, default=TypeOfOffer.RENT
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Property Listings"

    def get_absolute_url(self):
        return reverse('properties', args=[str(self.id)])


class PropertyListImages(models.Model):
    property = models.ForeignKey(PropertyListModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="property-list/carousel/images/")

    def __str__(self):
        return self.property.name

    class Meta:
        verbose_name_plural = "Carousel Images"


class PeopleModel(models.Model):
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    image = models.ImageField(upload_to="people/images/")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "People"
