from django.urls import path, include
from .views import products, detail_view

urlpatterns = [
    path('', products),
    path('detail_view/<int:pk>/', detail_view)
]