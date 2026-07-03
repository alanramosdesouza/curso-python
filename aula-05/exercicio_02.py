import requests

cep = input("Digite o CEP (somente números): ")
resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
if resposta.status_code == 200:
    dados = resposta.json()
    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print(f'CEP: {dados["cep"]}')
        print(f'Logradouro: {dados["logradouro"]}')
        print(f'Bairro: {dados["bairro"]}')
        print(f'Cidade: {dados["localidade"]}')
        print(f'Estado: {dados["uf"]}')
else:  
    print("Erro ao consultar o API.")