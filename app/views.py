from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hardik(request):
    return HttpResponse('<h1><marquee>hardik pandya is best allrounder<h1>')

def gill(reqest):
    return HttpResponse('<h1>shubman gill is the prince of cricket<h1>')
