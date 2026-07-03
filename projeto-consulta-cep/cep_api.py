import requests

def consultar_cep(cep):
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    
    if resposta.status_code != 200:
        return None
    
    dados = resposta.json()

    if "erro" in dados:
        return None
    
    return dados