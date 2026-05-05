from django.urls import path
from . import views

urlpatterns = [
    # The 'name' here is what redirect('wheel-timer') looks for
    path('Hello,Mr.Toney!!', views.timer_page, name='wheel-timer'),
]