from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response({
        "books": "/api/books/",
        "members": "/api/members/",
        "borrow_records": "/api/borrow-records/",
        "categories": "/api/categories/",
        "swagger": "/swagger/",
        "redoc": "/redoc/",
    })
schema_view = get_schema_view(
    openapi.Info(
        title="Library Management System API",
        default_version='v1',
        description="API documentation for the Library Management System",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api-auth/', include('rest_framework.urls')),

    path('api/auth/', include('djoser.urls')),     
    path('api/auth/', include('djoser.urls.jwt')), 

    path('api/books/', include('books.urls')),
    path('api/members/', include('members.urls')),
    path('api/borrow-records/', include('borrow.urls')),
    path('api/categories/', include('categories.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


