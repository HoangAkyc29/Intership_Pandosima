from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('myhospital/',include('myhospital.urls')),
    path('admin/', admin.site.urls),
]