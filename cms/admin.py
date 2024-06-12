from django.contrib import admin

from cms.models import PeopleModel, PropertyListImages, PropertyListModel


class PropertyListImagesInline(admin.StackedInline):
    model = PropertyListImages
    extra = 0
    fieldsets = (('Text Fields', {'fields': ('image',)}),)


class PropertyListModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'type_of_property',
        'type_of_offer',
        'floor_size',
        'number_of_bedrooms',
        'number_of_bathroom',
    ]
    inlines = [PropertyListImagesInline]


admin.site.register(PropertyListModel, PropertyListModelAdmin)


class PeopleAdmin(admin.ModelAdmin):
    list_display = ["name", "role"]


admin.site.register(PeopleModel, PeopleAdmin)
