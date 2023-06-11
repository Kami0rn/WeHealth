from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def treat(request):
    return render(request,"treat.html")

def trainer(request):
    return render(request,"trainer.html")

def chat(request):
    return render(request,"chat.html")

def info(request):
    return render(request,"info.html")