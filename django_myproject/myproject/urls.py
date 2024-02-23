from django.contrib import admin
from django.urls import path,include
import myapp,myapp2,videostream

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('myapp2/', include('myapp2.urls')),
    path('accounts/', include('user_management.urls')),
    path('videostream/', include('videostream.urls')),
]
