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
from django.conf.urls.static import static
from core import views as core_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("registration.backends.simple.urls")),
    path('', core_views.gallery_list, name="gallery_list"),
    path('gallery/<int:pk>/', core_views.gallery_detail, name="gallery_detail"),
    path('gallery/create/', core_views.gallery_create, name="gallery_create"),
    path('gallery/<int:pk>/delete/', core_views.gallery_delete, name="gallery_delete"),
    path('gallery/<int:pk>/add_photo/', core_views.add_photo, name="add_photo"),
    path('photo/list_photo/', core_views.list_photo, name="list_photo"),
    path('gallery/<int:pk>/delete_photo/', core_views.delete_photo, name='delete_photo')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
