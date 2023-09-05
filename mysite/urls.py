from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core.views import home_view, about_view, contact_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("contact/", contact_view, name="contact")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
