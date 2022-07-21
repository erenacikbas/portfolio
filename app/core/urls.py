"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import index_page, blog_page, journal_page, blog_about_page, blog_contact_page, blog_category_page
from django.views.decorators.cache import cache_page

# Login Views

from blog.views import BlogPostDetailView, BlogPostListView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    # Django Admin
    path('admin/', admin.site.urls),

    # User Management
    path('accounts/', include('django.contrib.auth.urls')),

    # Home Page
    path('', cache_page(60*15)(index_page), name='portfolio'),
    
    # Blog Page
    path('blog/', BlogPostListView.as_view(), name='blog'),
    path('blog/post/<slug:slug>', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/category/', blog_category_page, name='blog_category'),
    path('blog/about/', blog_about_page, name='blog_about'),
    path('blog/contact/', blog_contact_page, name='blog_contact'),

    # Journal Page
    path('journal/', journal_page, name='journal'),

    # Signup Page for CustomUser Model
    path('accounts/', include('users.urls')),

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
