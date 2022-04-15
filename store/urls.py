from django.urls import path
from . import views


urlpatterns = [
    path('', views.StoreListAPIView.as_view(), name="store"),
    path('<int:id>', views.StoreDetailAPIView.as_view(), name="store"),
]
