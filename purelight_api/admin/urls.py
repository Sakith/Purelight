from rest_framework.routers import DefaultRouter
from admin_api import *
from rest_framework import urls
from django.conf.urls import url , include


router = DefaultRouter()

router.register(r'admin', Admin_viewsets)
router.register(r'user', User_viewsets)
router.register(r'role', User_role_viewsets)
router.register(r'customer', Customer_viewsets)
router.register(r'healer' , Healer_viewsets)
router.register(r'media' , Media_viewsets)
router.register(r'track' , Track_viewsets)
router.register(r'offers' , Offers_viewsets)
router.register(r'purchases' , Purcahses_viewsets)
router.register(r'download-details' , Download_viewsets)

urlpatterns = router.urls
