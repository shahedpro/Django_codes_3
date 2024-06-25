from django.urls import path
from .views import HomePageView, CarDetailView, buy_car

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/buy/', buy_car, name='buy_car'),
]
