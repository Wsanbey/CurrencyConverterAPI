from django.urls import path
from app_CurrencyConverterAPI import views

urlpatterns = [
    path('', views.home, name='home'),  # Rota existente, apenas como demonstração do sistema
    path('convert', views.convert, name='convert'),  # Rota para a conversão monetária
]
