from ads.views.ad import ad, AdViewSet,  ADUploadImage
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # path('<int:pk>', ADDetailView.as_view(),),
    # path('<int:pk>/delete/', ADDeleteView.as_view(),),
    # path('<int:pk>/update/', ADUpdateView.as_view(),),
    # path('<int:pk>/create/', ADCreateView.as_view(),),
    path('<int:pk>/upload_image/', ADUploadImage.as_view(),),
]