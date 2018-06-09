#configure urls
from django.urls import path

from . import views

urlpatterns = [
    path('', views.page2Home, name='page2_home'),
]