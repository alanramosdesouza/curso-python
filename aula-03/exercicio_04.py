try:
    with open("aula-03/usuarios.txt", "r", encoding="utf-8") as arquivo:
        usuarios = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print("Usuários cadastrados:")
    print(usuarios)