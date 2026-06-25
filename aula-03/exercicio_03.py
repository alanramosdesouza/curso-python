nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
with open("aula-03/cadastros.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome: {nome}, Idade: {idade}\n")

print("\nPessoas cadastradas:")

with open("aula-03/cadastros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())