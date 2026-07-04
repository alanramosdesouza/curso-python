class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


alan = Pessoa("Alan", 36)
maria = Pessoa("Maria", 28)

print(maria.apresentar())
print(alan.apresentar())