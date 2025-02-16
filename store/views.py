from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Game

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    games = Game.objects.all()
    return render(request, 'store/home.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'store/game_detail.html', {'game': game})

def add_to_cart(request, game_id):
    cart = request.session.get('cart', {})  # Get cart from session
    cart[str(game_id)] = cart.get(str(game_id), 0) + 1  # Increase quantity
    request.session['cart'] = cart  # Save cart
    messages.success(request, "Game added to cart!")
    return redirect('cart')

def remove_from_cart(request, game_id):
    cart = request.session.get('cart', {})
    if str(game_id) in cart:
        del cart[str(game_id)]
    request.session['cart'] = cart
    messages.success(request, "Game removed from cart!")
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    games = Game.objects.filter(id__in=cart.keys())  # Get games in cart
    cart_items = [{'game': game, 'quantity': cart[str(game.id)]} for game in games]
    total_price = sum(item['game'].price * item['quantity'] for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request):
    return render(request, 'store/checkout.html')