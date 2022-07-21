from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


# Create your views here.
def index_page(request):
    return render(request, "portfolio/index.html")


def blog_page(request):
    return render(request, "blog/index.html")


def blog_about_page(request):
    return render(request, "blog/about.html")


def blog_contact_page(request):
    return render(request, "blog/contact.html")


def blog_category_page(request):
    return render(request, "blog/category.html")


def journal_page(request):
    return render(request, "journal/single.html")
