from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.Index),
    url(r'^articles/', include(admin.site.urls)),
]
