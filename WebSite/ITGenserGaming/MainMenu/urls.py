from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_games', views.about_games, name='about_games'),
    path('about_programming', views.about_programming, name='about_programming'),
    path('my_work', views.my_work, name='my_work'),
]