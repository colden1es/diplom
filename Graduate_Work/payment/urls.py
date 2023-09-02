from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/buy/', views.item_buy, name='item_buy'),
    path('payment_received/', views.payment_received, name='payment_received'),
]
