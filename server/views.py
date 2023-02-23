from django.shortcuts import render
from django.http import HttpResponse
def data(request):
    if request.method=="GET":
        return HttpResponse("<h1>data Get</h1>")

def get_data(request):
    if request.method=="POST":
        print(request)
        return HttpResponse("<h1>data post </h1>")
