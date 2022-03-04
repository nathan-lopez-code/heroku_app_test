from django.shortcuts import render
from datetime import date
from .models import Me
from .forms import ContactMe


def index(request):
    me = Me.objects.get(pk=1)
    age = date.today().year - me.birth
    me = {
        'me' : me,
        'age' : age,
    }
    return render(request, template_name="portfolio/index.html", context=me)


def contact(request):

    name = None
    me = Me.objects.get(pk=1)

    if request.method == 'POST':
        form = ContactMe(request.POST)
        if form.is_valid():
            name = request.POST['name']

            return render(request, template_name="portfolio/contact.html", context=me)


    else:
        form = ContactMe()
    


   
    context = {
        'me' : me,
        'form' : form,
    }

    return render(request, template_name="portfolio/contact.html", context=context)