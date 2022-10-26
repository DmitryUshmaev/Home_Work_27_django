from ads.views.category import CategoryDetailView, CategoryListView, CategoryUpdateView, CategoryDeleteView, \
    CategoryCreateView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path




urlpatterns = [
    path('', CategoryListView.as_view(),),
    path('<int:pk>', CategoryDetailView.as_view(),),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), ),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), ),
    path('<int:pk>/create/', CategoryCreateView.as_view(), ),
]