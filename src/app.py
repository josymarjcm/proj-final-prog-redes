from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields
from banco_de_dados import BancoDeDados
import json

app = Flask(__name__)
api = Api(app, version = "1.0", title = "Trabalho",
    description = "API")

ns = api.namespace("api", description = "Operacoes")
banco = BancoDeDados()

"""
Função para inserção da humidade no banco de dados.
Retorna um código 200 para informar ao usuário da ação bem sucedida.
"""
@ns.route("/inserir_humidade/<valor>")
class InserirHumidade(Resource):
    def post(self, valor):
        return banco.inserir_humidade(valor)

"""
Função para inserção da temperatura no banco de dados.
Retorna um código 200 para informar ao usuário da ação bem sucedida.
"""
@ns.route("/inserir_temperatura/<valor>", methods = ["POST"])
class InserirTemperatura(Resource):
    def post(self, valor):
        return banco.inserir_temperatura(valor)

"""
Função para inserção do gás no banco de dados.
Retorna um código 200 para informar ao usuário da ação bem sucedida.
"""
@ns.route("/inserir_gas/<valor>")
class InserirGas(Resource):
    def post(self, valor):
        return banco.inserir_gas(valor)

"""
Recebe parâmetros e retorna os dados em formato JSON baseado nos mesmos.
Retornos: dados e média(s).
"""
@ns.route("/selecionar/<humidade>/<temperatura>/<gas>/<de>/<ate>")
class Selecionar(Resource):
    def get(self, humidade, temperatura, gas, de, ate):
        if humidade == "False":
            humidade = False
        else:
            humidade = True

        if temperatura == "False":
            temperatura = False
        else:
            temperatura = True

        if gas == "False":
            gas = False
        else:
            gas = True

        dados, flag = banco.selecionar_dados(humidade, temperatura, gas, de, ate)

        if not dados:
            return 404

        media = 0
        if not flag:
            for i in dados:
                media += i[1]

            media = media / len(dados)
            dados.append(media)
        else:
            media_tem = 0
            media_hum = 0
            media_gas = 0

            for i in dados[1]:
                media_tem += i[-1]

            for i in dados[0]:
                media_hum += i[-1]

            for i in dados[2]:
                media_gas += i[-1]

            media_tem = media_tem / len(dados[1])
            media_hum = media_hum / len(dados[0])
            media_gas = media_gas / len(dados[2])

            dados.append(media_tem)
            dados.append(media_hum)
            dados.append(media_gas)

        return jsonify(dados)

"""
Método principal para iniciar o programa.
"""
if __name__ == "__main__":
    app.run("10.24.13.102", debug = True)
