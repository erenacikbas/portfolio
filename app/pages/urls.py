from django.urls import path, include
from django.views.decorators.cache import cache_page
from .views import index_page

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', cache_page(60 * 15)(index_page), name='portfolio'),
]
