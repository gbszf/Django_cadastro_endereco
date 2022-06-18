from django.shortcuts import render
from .models import CEP 

# Create your views here.
def pag_inicial(request):
	
	"""get_cep = CEP.objects.get(cep=cep).cep
			    context = {
			    'nome': get_nome,
			    'email': get_email,
			    'cep': get_cep,
			    'endereco': get_endereco,
			    'numero': get_num,
			    'bairro': get_bairro,
			    'cidade': get_cidade,
			    'uf': get_uf
			
			    }"""
	get_end = CEP.objects.all()

	return render(request, template_name='pagina inicial/index.html', context={'endereco':get_end})

def pag_cadastro(request):
	return render(request, template_name="pagina de cadastro/cadastro.html")