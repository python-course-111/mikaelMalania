from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    # return render(request, 'home.html', {})
    return HttpResponse("<h1>Hello World!</h1>")
