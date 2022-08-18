from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'mainmenu/index.html')

def about_games(request):
    return render(request, 'mainmenu/about_games.html')

def about_programming(request):
    return render(request, 'mainmenu/about_programming.html')

def my_work(request):
    return render(request, 'mainmenu/my_work.html')