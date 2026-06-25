tarefa = input("Digite a tarefa que deseja adicionar: ")
with open("aula-03/tarefas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{tarefa}\n")
    print("Tarefa adicionada com sucesso!")
with open("aula-03/tarefas.txt", "r", encoding="utf-8") as arquivo:
    print("\nTarefas cadastradas:")
    for numero, linha in enumerate(arquivo, start=1):
        print(f"{numero}. {linha.strip()}")