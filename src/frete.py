import json


def coletar_opcoes():
    with open("./src/opcoes.json", "r") as opcoes_texto:
        opcoes = json.loads(opcoes_texto.read())

    return opcoes


def calcular_frete(dimensao, peso):
    opcoes_frete_disponiveis = coletar_opcoes()
    opcoes = []

    for opcao in opcoes_frete_disponiveis:
        print(opcao)
        if (opcao["dimensao"]["alt_min"] <= dimensao["altura"] <= opcao["dimensao"]["alt_max"] and
                opcao["dimensao"]["larg_min"] <= dimensao["largura"] <= opcao["dimensao"]["larg_max"]):
            opcoes.append(
                {
                    "nome": opcao["nome"],
                    "valor_frete": (peso * opcao["constante"]) / 10,
                    "prazo_dias": opcao["prazo"]
                }
            )

    return opcoes
