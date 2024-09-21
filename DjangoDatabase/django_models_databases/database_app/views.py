from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    musicians_data = models.Musician.objects.all()
    musicians_context = {"musicians": musicians_data}
    return render(request, 'database_app/index.html', context=musicians_context)
