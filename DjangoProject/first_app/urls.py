from django.urls import path
from . import  views

urlpatterns = [
    path("about", views.index, name="index"),
    path("course/<int:number>/", views.course_index, name="course_index"),
    path("course_number/<int:course_index>/", views.course_number_view, name="course_number_view"),
    path("<str:item>/", views.course, name="course" ),
    path("<int:number1>/<int:number2>/<int:number3>/",views.multiply, name="multiply"),
    path("<str:item>/other", views.other_courses, name="other_courses"),


]
