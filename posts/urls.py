from django.urls import path
# from posts import views
from . import views

urlpatterns = [
    path('', views.home),
    path('pass/', views.passView),
]
