from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order

class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
