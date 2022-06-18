from django.urls import path
from endereco import views

urlpatterns = [
    path('', views.pag_inicial),
    path('', views.pag_cadastro, name="cadastro"),
    
]