from django.shortcuts import render
from datetime import date
from .models import Me


def index(request):
    me = Me.objects.get(pk=1)
    age = date.today().year - me.birth
    me = {
        'me' : me,
        'age' : age,
    }
    return render(request, template_name="portfolio/index.html", context=me)


def contact(request):
    me = Me.objects.get(pk=1)
    me = {
        'me' : me,
    }
    return render(request, template_name="portfolio/contact.html", context=me)