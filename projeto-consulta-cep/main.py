from cep_api import consultar_cep
from historico import salvar_consulta
from historico import listar_historico

while True:
    print("\n=== Consulta de CEP ===")
    print("1 - Consultar CEP")
    print("2 - Ver histórico")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cep = input("Digite o CEP (somente números): ")
        dados = consultar_cep(cep)
        if dados is None:
            print("CEP não encontrado ou inválido.")
        else:
            print(f'CEP: {dados["cep"]}')
            print(f'Logradouro: {dados["logradouro"]}')
            print(f'Bairro: {dados["bairro"]}')
            print(f'Cidade: {dados["localidade"]}')
            print(f'Estado: {dados["uf"]}')

            
            salvar_consulta(dados)
            print("Consulta salva no histórico.")
    elif opcao == "2":
        listar_historico()
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
