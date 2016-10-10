from django.shortcuts import render
from rango.models import Category, Page
from django.http import HttpResponse
from django.http import HttpRequest


def index(request):
    context_dict = {}
    try:
        category_list = Category.objects.order_by('-likes')[:5]
        pages_list = Page.objects.order_by('-views')[:5]
        context_dict['pages'] = pages_list
        context_dict['categories'] = category_list

    except Category.DoesNotExist:
        context_dict['categories'] = None
        context_dict['pages'] = None
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', context=None)
    # return HttpResponse("Rango says here is the about page <a href='/rango'> back  </a>")


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
