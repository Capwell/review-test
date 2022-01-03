from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Item


def index(request):
    template = loader.get_template('index.html')    
    context = {
        'items': Item.objects.filter(on_main=True)
    }
    return HttpResponse(template.render(context, request))


def list(request, category_slug):
    template = 'list.html'
    context = {
    }
    return render(request, template, context)


def detail(request, category_slug, id):
    return render(request, 'detail.html', {})
