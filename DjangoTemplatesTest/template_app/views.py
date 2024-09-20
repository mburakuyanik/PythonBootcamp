from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"template_app/first.html")

def weather_app(request):
    weather_dict = {"istanbul": "30 ",
                    "malatya" : "44",
                    "izmir"   : [5,20,30,40],
                    "ankara"  : {"morning" : 10, "evening": 20},
                    "user_premium": True,
                    "test": "test Test test Test"
                    }
    return render(request, "template_app/weather.html", context=weather_dict)

