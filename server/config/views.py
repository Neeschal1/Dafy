from django.http import HttpResponse

def home(request):
    return HttpResponse('This is the home UI. welcome!')