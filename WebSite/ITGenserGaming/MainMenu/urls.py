from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_games', views.about_games, name='about_games'),
    path('about_programming', views.about_programming, name='about_programming'),
    path('my_work', views.my_work, name='my_work'),

    path('about_games/PC', views.PC, name='about_games/PC'),
    path('about_games/Android', views.Android, name='about_games/Android'),
    path('about_games/PlayStation', views.PlayStation, name='about_games/PlayStation'),
    path('about_games/IOS', views.IOS, name='about_games/IOS'),
]