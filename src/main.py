from flask import Flask, request, Response, g
import json
import frete as frete


app = Flask(__name__)


@app.before_request
def validar_post():
    if request.method == 'POST':
        if not request.content_type == 'application/json':
            return Response("Corpo da requisição deve ser application/json", 400)
        else:
            g.claims = json.loads(request.get_data())


@app.route('/')
def server_status():
    return 'Server\'s running'


@app.route('/consultar_frete', methods=['POST'])
def consultar_frete():
    if g.claims["peso"] <= 0:
        return Response("Peso do pacote não pode ser 0", 400)

    opcoes_frete = frete.calcular_frete(g.claims['dimensao'], g.claims['peso'])
    print(opcoes_frete)
    return Response(json.dumps(opcoes_frete, ensure_ascii=False), 200)


if __name__ == '__main__':
    app.run(port=8080)
