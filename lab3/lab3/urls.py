from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wheel_timer.urls')), # This imports the app urls
    path('', lambda request: redirect('wheel-timer')), 
]