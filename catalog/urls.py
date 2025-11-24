from django.urls import path

from catalog.views import home, contacts, base

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('base/', base, name='base'),
]
