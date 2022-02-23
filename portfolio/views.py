from django.shortcuts import render


def index(request):
    return render(request, template_name="portfolio/index.html", context=None)
