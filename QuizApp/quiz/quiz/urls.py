
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('api/',include('home.urls'))
    
]
