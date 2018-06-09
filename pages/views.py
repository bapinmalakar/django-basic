from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('Hello, World!');
def getAuthorName(request):
    return HttpResponse('Author Name Biplab Malakar');