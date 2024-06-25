from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.OrderHistoryView.as_view(), name='order_history'),
]
