import requests

usuario = input("Digite o nome de usuário do GitHub: ")
resposta = requests.get(f"https://api.github.com/users/{usuario}")

if resposta.status_code == 200:
    dados = resposta.json()
    dados = resposta.json()
    print(f'Usuário: {dados["login"]}')
    print(f'Nome: {dados["name"]}')
    print(f'Repositórios públicos: {dados["public_repos"]}')
    print(f'Perfil: {dados["html_url"]}')
else:
    print("Usuário não encontrado.")