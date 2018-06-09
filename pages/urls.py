#configure urls
from django.urls import path

from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('author_name', views.getAuthorName, name='author_name'),
    path('about/', views.AboutPageView.as_view(), name="about"),
]