frase = input("Digite uma frase: ")
with open("aula-03/mensagem.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f'\n{frase}')

