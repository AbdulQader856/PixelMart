from django.urls import path
from .views import signup_user, login_user, logout_user, home

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_user, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
