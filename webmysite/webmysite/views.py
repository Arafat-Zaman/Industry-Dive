# I have created this file - arafat
from django.http import HttpResponse

def index(request):
     return HttpResponse('''<h1>hello arafat</h1> <a href="https://www.youtube.com/">Youtube click on here</a>''')

def about(request):
    return HttpResponse("<h1>hello arafat</h1>")

def about(request):
    return HttpResponse("about hello arafat01")

