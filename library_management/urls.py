from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('api/', include('books.urls')),       
    path('api/', include('members.urls')),     
    path('api/', include('borrow.urls')),
    
]
