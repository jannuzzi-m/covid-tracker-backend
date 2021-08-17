from django.urls import path
from api import views

urlpatterns = [
    path('hello/', views.HelloWorld.as_view()),
]