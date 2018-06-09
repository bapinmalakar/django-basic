from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
     template_name = 'home.html';


# def homePageView(request):
#     return HttpResponse('Hello, World!');
def getAuthorName(request):
    return HttpResponse('Author Name Biplab Malakar');