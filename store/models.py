from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    CATEGORY_CHOICES = [
        ('latest', 'Latest Releases'),
        ('top', 'Top Selling'),
        ('upcoming', 'Upcoming'),
    ]

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='game_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='latest')

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.game.title}"