from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.models import Location
# from users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, LocationViewSet

# router = routers.SimpleRouter()
# router.register('location', LocationViewSet)
#
# urlpatterns = [
#     path('', UserListView.as_view(), ),
#     path('<int:pk>/', UserDetailView.as_view(), ),
#     path('<int:pk>/update/', UserUpdateView.as_view(), ),
#     path('create/', UserCreateView.as_view(), ),
#     path('<int:pk>/delete/', UserDeleteView.as_view(), ),
# ]
#
# urlpatterns += router.urls


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),),
    path('token/refresh/', TokenRefreshView.as_view(), ),
]