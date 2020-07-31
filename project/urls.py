"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as photo_views
from django.conf.urls import include

urlpatterns = [
    path('', photo_views.home, name='home'),
    path('photos/<int:pk>', photo_views.show_photo, name='show_photo'),
    path('photos/add/', photo_views.add_photo, name='add_photo'),
    path('photos/<int:pk>/favorite/', photo_views.favorite_photo, name='favorite_photo'),
    path('photos/<int:pk>/delete/', photo_views.delete_photo, name='delete_photo'),
    path('albums/', photo_views.list_albums, name='list_albums'),
    path('albums/add/', photo_views.add_album, name='add_album'),
    path('albums/<int:pk>/add/photo/', photo_views.add_photo_to_album, name='add_photo_to_album'),
    path('albums/<int:pk>/favorite/', photo_views.favorite_album, name='favorite album'),
    path('albums/<int:pk>/', photo_views.show_album, name='show_album'),
    path('albums/<int:pk>/delete', photo_views.delete_album, name='delete_album'),
    path('albums/search/', photo_views.search_photos, name='search_photos'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
