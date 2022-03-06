from django.shortcuts import render
from datetime import date
from .models import Me
from .forms import ContactMe
from django.core.mail import send_mail
from django.conf import settings



me = Me.objects.get(pk=1)

def index(request):
    age = date.today().year - me.birth
    context = {
        'me' : me,
        'age' : age,
    }
    return render(request, template_name="portfolio/index.html", context=context)


def contact(request):

    name = None
    if request.method == 'POST':
        form = ContactMe(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['messages']
            recipe = settings.EMAIL_HOST_USER


            # sending email

            send_mail(
                f"subject : {subject}",
                f"message\n \n from : {email}\nmame: {name}",
                email,
                [recipe]
            )

            # add name in context
            context = {
                "me" : me,
                "name" : name,
            }

            return render(request, template_name="portfolio/contact.html", context=context)


    else:
        form = ContactMe()
    

    context = {
        'me' : me,
        'form' : form,
    }

    return render(request, template_name="portfolio/contact.html", context=context)