from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home_view, about_view, blog_view, theme_view, post_view


urlpatterns = [
    path("admin/", admin.site.urls),
    # Members
    path("members/", include("members.urls")),
    # Core
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("blog/", blog_view, name="blog"),
    path("theme/", theme_view, name="theme"),
    path("post/", post_view, name="post"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
