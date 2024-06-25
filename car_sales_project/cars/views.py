from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from .models import Car, Brand, Comment
from .forms import CommentForm
from orders.models import Order

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        brand = self.request.GET.get('brand')
        if brand:
            context['cars'] = Car.objects.filter(brand__name=brand)
        else:
            context['cars'] = Car.objects.all()
        return context

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.car = car
            comment.save()
        return self.get(request, *args, **kwargs)

def buy_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.quantity > 0:
        Order.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
    return redirect('profile')
