from django.urls import path

from cms.views import (
    ComingSoonView,
    ContactUsView,
    HomePageView,
    PropertyListPageDetailView,
    PropertyListPageListView,
    SellView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("properties", PropertyListPageListView.as_view(), name="properties"),
    path(
        'properties/<int:pk>/',
        PropertyListPageDetailView.as_view(),
        name='properties-details',
    ),
    path("contact", ContactUsView.as_view(), name="contact"),
    path("coming-soon", ComingSoonView.as_view(), name="coming-soon"),
    path("sell", SellView.as_view(), name="sell"),
]
