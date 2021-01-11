from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.listing), # "/store" will call the method "index" in "views.py"
]