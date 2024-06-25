from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='orders')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
