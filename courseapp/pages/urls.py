from django.http import HttpResponse
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('index',views.index),
    path('iletisim', views.iletisim),
    path('hakkimizda', views.hakkimizda),
]