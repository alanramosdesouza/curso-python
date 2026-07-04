class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade

livro = Produto("Livro", 50.00, 3)
caneta = Produto("Caneta", 2.50, 10)

total_caneta = caneta.calcular_valor_total()
total_livro = livro.calcular_valor_total()

print(f'Produto: {caneta.nome}')
print(f'Total em estoque: {total_caneta:.2f}')
print(f'Produto: {livro.nome}')
print(f'Total em estoque: {total_livro:.2f}')