from django.contrib import admin
from django.urls import path

# to provide url in old fashion way
from django.conf.urls import  url, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # redirects the url to shortit urls
    url(r'', include('shortit.urls')),
    
]
