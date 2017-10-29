from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def http_404(request):
    return render(request, '404.html')
