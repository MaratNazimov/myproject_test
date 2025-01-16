from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('process/<int:feed_id>/', views.process_image_feed, name='process_feed'),
    path('add-image-feed/', views.add_image_feed, name='add_image_feed'),
    path('image/delete/<int:image_id>/', views.delete_image, name='delete_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)