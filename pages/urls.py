#configure urls
from django.urls import path

from . import views
urlpatterns = [
    path('', views.homePageView, name='home'),
    path('author_name', views.getAuthorName, name='author_name'),
]