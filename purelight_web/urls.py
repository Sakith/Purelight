from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^healer/$' , views.Login.as_view() , name='admin_login'),

    #brows urls
    url(r'^healer/browse/$' , views.Browse.as_view(), name='browse'),
    url(r'^healer/browse/detial/package/(?P<media_id>[\w.@+-]+)/$' , views.Browse.PackageDetail.as_view()),
    url(r'^healer/browse/detial/track/(?P<track_id>[\w.@+-]+)/$' , views.Browse.MusicDetail.as_view()),

    # #update urls
    # url(r'^healer/browse/detial/edit-audio/(?P<track_id>\d+)/$'),
    url(r'^healer/browse/detial/edit-package/(?P<media_id>\d+)/$' ,views.EditAudioPackage.as_view()),
    #
    # #create urls
    # url(r'^healer/addMusic'),
    # url(r'^healer/addPackage'),
]