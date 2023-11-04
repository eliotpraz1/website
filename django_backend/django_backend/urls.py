

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *
 
router = routers.DefaultRouter()
router.register('aboutme', AboutMeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),
]