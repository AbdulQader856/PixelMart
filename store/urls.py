from django.urls import path
from .views import signup_user, login_user, logout_user, home, game_detail

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_user, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
]
