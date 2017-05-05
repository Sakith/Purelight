from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^admin/$' , views.Login.as_view() , name='admin_login'),
    url(r'^admin/addmusic/', views.addMusic , name='add_music'),
    url(r'^admin/brows/$' , views.brows , name='brows')
]