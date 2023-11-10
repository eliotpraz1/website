

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *
 
router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)
router.register('person', PersonViewSet)
router.register('subject', SubjectViewSet)
router.register('comment', CommentViewSet)


urlpatterns = [

    path('admin/', admin.site.urls),    
    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]