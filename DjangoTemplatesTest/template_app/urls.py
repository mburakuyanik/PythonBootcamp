from django.urls import path
from . import views

app_name = 'template_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.weather_app, name='weather_app')

]