# importing loading from django template
from django.views import View
from django.template import loader, RequestContext
from django.shortcuts import render
from purelight.models import *
from django.http import HttpResponseRedirect



class Login(View):
    def get(self , request, *args , **kwargs):
        return render(request , "login.html" , {})

    def post(self , request, *args , **kwargs):
        userl = User.objects.get(name=request.POST.get('email'))

        if  userl == None:
            print ("No email found")
            return render(request, "login.html", {})
        else:
            print ("email found")
            if userl.password == request.POST.get('password'):
                print ("User logged in")
                healer = Healer.objects.get(user=userl.userid)
                return HttpResponseRedirect('browse/'+'?healer_id='+str(healer.healerid))
            else:
                print ("Wrong user name or password")
                return render(request , "login.html" , {})
        # print [request.POST.get('email')]
        # print [request.POST.get('password')]
        #
        # return render(request , "login.html" , {})


class AddMusic(View):
    def get(self ,request, *args, **kwargs):
        request.POST
        return render(request , "add_audio.html", {})

class Browse(View):
    def get(self , request):
        medialist = []
        media = Media.objects.filter(healer_id=request.GET.get('healer_id'))
        healer = Healer.objects.get(healerid=request.GET.get('healer_id'))


        return render(request , "brows_audio.html" , {"media" : media , "healer" : healer})

    class PackageDetail(View):
        def get(self , request, media_id):
            medias = Media.objects.get(mediaid=media_id)
            return render(request, "brows_audio.html", medias)

    class MusicDetail(View):
        def get(self , request, healer_id):
            return None


class AddAudioPackage(View):
    def get(self):
        return None

class EditAudio(View):
    def get(self):
        return None

class EditAudioPackage(View):
    def get(self , request):
        return render(request, "edit_audio_package.html")

    def post(self , request):
        return render(request, "edit_audio_package.html")

class MySales(View):
    def get(self):
        return None