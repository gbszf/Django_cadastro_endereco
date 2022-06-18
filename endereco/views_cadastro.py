from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import CEP 
from django.shortcuts import redirect


# Create your views here.
def get_data(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    cep = request.POST.get('cep')
    endereco = request.POST.get('endereco')
    numero = request.POST.get('numero')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    uf = request.POST.get('uf')
    descricao = request.POST.get('descricao')
    
    get_cep = ""
   
    try:
        get_cep = CEP.objects.get(cep=cep).cep
    except CEP.DoesNotExist:
        pass
   
    if cep == get_cep:
        get_id = CEP.objects.get(cep=cep).id
        get_endereco = CEP.objects.get(id=get_id)
        get_endereco.cep = cep 
        get_endereco.nome = nome 
        get_endereco.email = email 
        get_endereco.descricao = descricao
        get_endereco.endereco = endereco
        get_endereco.numero = numero 
        get_endereco.cidade = cidade 
        get_endereco.uf = uf 
        get_endereco.bairro = bairro

        get_endereco.save(update_fields=['nome','email','cep','endereco','numero','bairro','cidade','uf','descricao' ])
       
        return redirect("../pagina inicial/")
    if cep:      
        cadastro_endereco = CEP(
                nome = nome,
                email = email,
                cep = cep,
                endereco = endereco,
                numero = numero,
                bairro = bairro,
                cidade = cidade,
                uf = uf,
                descricao = descricao
            )

        cadastro_endereco.save()
        
        enderecos_cadastrados = CEP.objects.get(cep=cep).cep
        
        return redirect("../pagina inicial/")
   
        



    return render(request, template_name='pagina de cadastro/cadastro.html')
