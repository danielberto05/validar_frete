
def validar_requisicao_frete(dados_pacote):
    if dados_pacote["peso"] <= 0:
        return "Peso do pacote não pode ser 0", 400
    else:
        return True
