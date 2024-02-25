from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import FromText


urlpatterns = [
    path('', views.index),
    path('fr', views.transQ, name='fr'),
    path('to', views.transQW, name='to'),
    path('text', csrf_exempt(FromText.as_view()), name='text')

]