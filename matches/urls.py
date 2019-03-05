from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'matches'
urlpatterns = [
    # path('upload/', upload),
    path('all_matches/', all_matches, name='all-matches'),
    path('load_excel/', load_excel, name='load-excel'),
    path('delete/', delete, name='delete-all'),
    path('', Index.as_view(), name='index')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)