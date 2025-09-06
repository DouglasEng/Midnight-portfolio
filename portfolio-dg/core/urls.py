"""
URLs do app portfolio.
Configuração das rotas para o site de portfólio noir.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos_list'),
]

