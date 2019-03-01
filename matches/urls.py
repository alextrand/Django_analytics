from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', index),
    # path('upload/', upload),
    path('all_matches/', all_matches),
    path('', Index.as_view(), name='index')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)