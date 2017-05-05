from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', include("purelight_api.admin.urls")),
#    url(r'^healer/', include("purelight_api.healer.urls")),
#     url(r'^user/', include("purelight_api.user.urls")),
 #  url(r'^auth/', include("purelight_api.auth.url")),
]
