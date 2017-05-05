# importing loading from django template
from django.views import View
from django.template import loader
from django.shortcuts import render



class Login(View):
    def get(self , request, *args , **kwargs):
        return render(request , "login.html" , {})

    def post(self , request, *args , **kwargs):
        print [request.POST.get('email')]



        return render(request , "login.html" , {})


def addMusic(request):
    return render(request , "add_audio.html")

def brows(request):
    return render(request , "brows_audio.html")

def addAudioPackage(request):
    return None

def editAudio(request):
    return None

def editAudioPackage(request):
    return None

def mySales(request):
    return None