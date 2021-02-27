from flask import Flask, request, Response, g
import json
import frete as frete
import utils as utils


app = Flask(__name__)


@app.before_request
def before_request_func():
    if request.method == 'POST':
        if not request.content_type == 'application/json':
            return Response("Corpo da requisição deve ser application/json", 400)
        else:
            claims = json.loads(request.get_data())
            if request.path == '/calcular_frete':
                validar_requisicao = utils.validar_requisicao_frete(claims)
                if validar_requisicao is not True:
                    return validar_requisicao

            g.claims = claims


@app.route('/')
def server_status():
    return 'Server\'s running'


@app.route('/calcular_frete', methods=['POST'])
def calcular_frete():
    opcoes_frete = frete.calcular_frete(g.claims['dimensao'], g.claims['peso'])
    print(opcoes_frete)
    return Response(json.dumps(opcoes_frete, ensure_ascii=False), 200)


if __name__ == '__main__':
    app.run(port=8080)
