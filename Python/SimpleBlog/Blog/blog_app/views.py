from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog_app/index.html')


def about(request):
    return render(request, 'blog_app/about.html')


def github(request):
    return render(request, 'blog_app/github.html')

def linkedin(request):
    return render(request, 'blog_app/linkedin.html')