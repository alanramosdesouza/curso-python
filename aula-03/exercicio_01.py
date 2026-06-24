with open("aula-03/mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Estou aprendendo a trabalhar com arquivos em Python!")
    
with open("aula-03/mensagem.txt",'r', encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)