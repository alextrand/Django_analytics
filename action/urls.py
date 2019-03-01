from django.urls import path, include
from .views import index, upload2, calc

urlpatterns = [
    path('upload/', upload2),
    path('form/', calc),
    # path('', index),
]