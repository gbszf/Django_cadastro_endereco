from django import template
register = template.Library()



"""import cgi, cgitb

def getDataForm():
	# Create instance of FieldStorage
	form = cgi.FieldStorage()
	# Get data from fields
	nome = form.getvalue('nome')
	email  = form.getvalue('email')
	cep = form.getvalue('cep')
	endereco = form.getvalue('endereco')
	numero = form.getvalue('numero')
	bairro = form.getvalue('bairro')
	cidade = form.getvalue('cidade')
	uf = form.getvalue('uf')

	print(cep)
	print(nome)
	print(email)
	print(endereco)

"""

