from django.urls import path
from .views import signup_user, login_user, logout_user, home, game_detail, cart, add_to_cart, remove_from_cart, checkout

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_user, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:game_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:game_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
]
