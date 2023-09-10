from django.shortcuts import render


def home_view(request):
    return render(request, "core/index.html")


def about_view(request):
    return render(request, "core/about.html")


def blog_view(request):
    return render(request, "core/blog.html")


def theme_view(request):
    return render(request, "components.html")


def post_view(request):
    return render(request, "core/post.html")
