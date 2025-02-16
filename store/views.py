import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Game, Order, OrderItem

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

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    cart = request.session.get('cart', {})
    total_price = sum(Game.objects.get(id=int(game_id)).price * qty for game_id, qty in cart.items())

    if request.method == "POST":
        # Create an order
        order = Order.objects.create(user=request.user, total_price=total_price, payment_status=False)

        # Save each cart item in OrderItem
        for game_id, quantity in cart.items():
            game = Game.objects.get(id=int(game_id))
            OrderItem.objects.create(order=order, game=game, quantity=quantity)

        # Create a Stripe checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': "PixelMart Purchase"},
                        'unit_amount': int(total_price * 100),
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="http://127.0.0.1:8000/success/",
            cancel_url="http://127.0.0.1:8000/cart/",
        )
        
        return redirect(session.url, code=303)

    return render(request, 'store/checkout.html', {'total_price': total_price, 'stripe_public_key': settings.STRIPE_PUBLIC_KEY})

def payment_success(request):
    last_order = Order.objects.filter(user=request.user).last()
    if last_order:
        last_order.payment_status = True
        last_order.save()
    
    request.session['cart'] = {}  # Clear the cart after payment
    return render(request, 'store/success.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_history.html', {'orders': orders})