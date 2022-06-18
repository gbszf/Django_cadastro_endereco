from django.urls import path
from endereco import views_cadastro


urlpatterns = [
    #path('', views_cadastro.cadastro),
    path('', views_cadastro.get_data),
    
    
    
]