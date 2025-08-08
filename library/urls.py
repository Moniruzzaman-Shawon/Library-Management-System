# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from .views import AuthorViewSet, CategoryViewSet, BookViewSet, MemberViewSet, BorrowRecordViewSet
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# router = DefaultRouter()
# router.register(r'authors', AuthorViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'books', BookViewSet)
# router.register(r'members', MemberViewSet)
# router.register(r'borrow-records', BorrowRecordViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#     path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('', include(router.urls)),
# ]
