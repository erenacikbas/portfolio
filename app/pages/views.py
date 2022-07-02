from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index_page(request):
    return render(request, "resume/index.html")

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

# Flare Template
@login_required
def template_1(request):
    return render(request, "flare/index.html")

# Tyndale Template
@login_required
def template_2(request):
    return render(request, "tyndale/index.html")

# Infinity Template
@login_required
def template_3(request):
    return render(request, "infinity/index.html")