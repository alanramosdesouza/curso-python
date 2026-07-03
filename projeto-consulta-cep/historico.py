def salvar_consulta(dados):
    with open("projeto-consulta-cep/historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f'{dados["cep"]} - {dados["logradouro"]}, {dados["bairro"]}, {dados["localidade"]}/{dados["uf"]}\n')
        
def listar_historico():
    try:
        with open("projeto-consulta-cep/historico.txt", "r", encoding="utf-8") as arquivo:
            consultas = arquivo.readlines()
            if len(consultas) == 0:
                print("Nenhuma consulta no histórico.")
            else:
                print("\nHistórico de consultas:")
                for numero, consulta in enumerate(consultas, start=1):
                    print(f"{numero}. {consulta.strip()}")
    except FileNotFoundError:
        print("Nenhum histórico encontrado.")