import requests
import sys
import os
import json
import random

"""
Converte o conteúdo do arquivo para JSON.
"""
def parser(arquivo):
	with open(arquivo) as f:
		dados = json.load(f)

	return dados

"""
Salva o conteúdo da resposta em um arquivo.
"""
def salvar_resposta(texto):
	nome = "arquivos_json/" + str(random.getrandbits(32)) + ".json"
	f = open(nome, "a")
	f.writelines(texto)

	return nome

"""
Verifica se a resposta contém algum conteúdo.
"""
def verificar_dados(texto):
	try:
		if int(texto) == 404:
		    os.system("cls" if os.name == "nt" else "clear")
		    print("\033[91m[-]\033[0m Dados não encontrados!")
		    return False
	except:
		return True

if not os.path.exists("arquivos_json"):
	os.makedirs("arquivos_json")
ip_servidor = "http://10.25.3.133:5000/"

try:
	r = requests.get(ip_servidor)
except:
	print("\033[91m[-]\033[0m Não foi possível se conectar ao servidor!")
	sys.exit(0)

while (True):
	print("Bem-vindo. Selecione a opção desejada:")
	print("1. Informações de temperatura")
	print("2. Informações de humidade")
	print("3. Informações de gás")
	print("4. Todas as informações")

	opcao = int(input(">> "))
	os.system("cls" if os.name == "nt" else "clear")

	if opcao not in [1, 2, 3, 4]:
	    print("Opção inválida!")
	    sys.exit(0)

	inicio = input("Início (formato: YYYY-MM-DD HH:MM:SS) >> ")
	fim = input("Fim (formato: YYYY-MM-DD HH:MM:SS) >> ")

	if opcao == 1:
	    r = requests.get("{}api/selecionar/False/True/False/{}/{}".format(ip_servidor, inicio, fim))
	    if not verificar_dados(r.text):
	        continue

	    print("\033[92m[+]\033[0m Dados obtidos!")
	    arquivo = salvar_resposta(r.text)
	    print("\033[92m[+]\033[0m Arquivo salvo em: \033[94m{}\033[0m".format(arquivo))
	    dados = parser(arquivo)
	    print("\033[92m[+]\033[0m Lendo dados do arquivo...")

	    print("\n\t=== Informações do sensor de temperatura === \n")
	    print("Valor de temperatúra médio: \t\t\033[92m{}°\033[0m\n".format(dados[-1]))
	elif opcao == 2:
		r = requests.get("{}api/selecionar/True/False/False/{}/{}".format(ip_servidor, inicio, fim))
		if not verificar_dados(r.text):
		    continue

		print("\033[92m[+]\033[0m Dados obtidos!")
		arquivo = salvar_resposta(r.text)
		print("\033[92m[+]\033[0m Arquivo salvo em: \033[94m{}\033[0m".format(arquivo))
		dados = parser(arquivo)
		print("\033[92m[+]\033[0m Lendo dados do arquivo...")

		print("\n\t=== Informações do sensor de humidade === \n")
		print("Valor de humidade médio: \t\t\033[92m{}\033[0m\n".format(dados[-1]))
	elif opcao == 3:
		r = requests.get("{}api/selecionar/False/False/True/{}/{}".format(ip_servidor, inicio, fim))
		if not verificar_dados(r.text):
		    continue

		print("\033[92m[+]\033[0m Dados obtidos!")
		arquivo = salvar_resposta(r.text)
		print("\033[92m[+]\033[0m Arquivo salvo em: \033[94m{}\033[0m".format(arquivo))
		dados = parser(arquivo)
		print("\033[92m[+]\033[0m Lendo dados do arquivo...")

		print("\n\t=== Informações do sensor de gás === \n")
		print("Valor de gás médio: \t\t\033[92m{}\033[0m\n".format(dados[-1]))
	else:
		r = requests.get("{}api/selecionar/True/True/True/{}/{}".format(ip_servidor, inicio, fim))
		if not verificar_dados(r.text):
		    continue

		print("\033[92m[+]\033[0m Dados obtidos!")
		arquivo = salvar_resposta(r.text)
		print("\033[92m[+]\033[0m Arquivo salvo em: \033[94m{}\033[0m".format(arquivo))
		dados = parser(arquivo)
		print("\033[92m[+]\033[0m Lendo dados do arquivo...")

		print("\n\t=== Informações dos sensores === \n")
		print("Valor de temperatura médio: \t\t\033[92m{}\033[0m".format(dados[-3]))
		print("Valor de humidade médio: \t\t\033[92m{}\033[0m".format(dados[-2]))
		print("Valor de gás médio: \t\t\t\033[92m{}\033[0m\n".format(dados[-1]))
