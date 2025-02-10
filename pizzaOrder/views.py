from django.shortcuts import render, redirect
from .forms import RegisterForm, PizzaOrderForm, DeliveryDetailForm, PizzaOrderFormSet
from .models import PizzaOrder, DeliveryDetail
from datetime import datetime, timedelta
from django.contrib.auth import login, authenticate
import uuid

def home(request):
    if request.user.is_authenticated:
        orders = PizzaOrder.objects.filter(user=request.user)
        return render(request, 'home.html', {'orders': orders})
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_pizza')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def create_pizza(request):
    if not request.user.is_authenticated:
        return redirect('login')   
    if request.method == 'POST':
        formset = PizzaOrderFormSet(request.POST)
        if formset.is_valid():
            order_id = uuid.uuid4()
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    pizza_order = form.save(commit=False)
                    pizza_order.user = request.user
                    pizza_order.order_id = order_id
                    pizza_order.save()
                    form.save_m2m()
            return redirect('delivery_details', pizza_order_id=order_id)
    else:
        formset = PizzaOrderFormSet()

    return render(request, 'create_pizza.html', {'formset': formset})

def delivery_details(request, pizza_order_id):
    pizza_order = PizzaOrder.objects.filter(order_id=pizza_order_id)

    if request.method == 'POST':
        form = DeliveryDetailForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.order_id = pizza_order_id
            delivery.save()
            return redirect('order_complete', pizza_order_id=pizza_order_id)
    else:
        form = DeliveryDetailForm()

    return render(request, 'delivery_details.html', {'form': form, 'pizza_order': pizza_order})

def order_complete(request, pizza_order_id):
    pizza_order = PizzaOrder.objects.filter(order_id=pizza_order_id)
    delivery = DeliveryDetail.objects.get(order_id=pizza_order_id)
    current_time = datetime.now()
    delivery_time = current_time + timedelta(minutes=30)
    print(pizza_order)
    return render(request, 'order_complete.html', {'pizza_order': pizza_order, 'delivery': delivery, 'delivery_time': delivery_time})
