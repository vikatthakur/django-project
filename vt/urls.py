from django import urls
from django.conf.urls import url
from django.urls.conf import include
import pages
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
