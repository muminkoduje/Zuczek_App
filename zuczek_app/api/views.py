from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("First Page")
def home1(request):
    return HttpResponse("<h1>Home Page</h1>")
