from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.CurrencyList.as_view(), name='currency-list'),
    path('rate/', views.CurrencyRateView.as_view(), name='currency-rate'),
]
