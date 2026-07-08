class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade
    
    def vender(self, quantidade_vendida):
        if quantidade_vendida <= 0:
            print('Quantidade inválida.')
        elif quantidade_vendida <= self.quantidade:
            self.quantidade -= quantidade_vendida
            print('Venda realizada.')
        else:
            print('Estoque insuficiente.')

    def repor(self, quantidade_reposta):
        if quantidade_reposta <= 0:
            print('Quantidade inválida.')
        else:
            self.quantidade += quantidade_reposta
            print('Estoque atualizado.')

livro = Produto("Livro", 50.00, 3)
caneta = Produto("Caneta", 2.50, 10)

total_caneta = caneta.calcular_valor_total()
total_livro = livro.calcular_valor_total()

print(f'Produto: {caneta.nome}')
print(f'Total em estoque: R$ {total_caneta:.2f}')
print(f'Produto: {livro.nome}')
print(f'Total em estoque: R$ {total_livro:.2f}')

livro.vender(2)

print(f"Quantidade restante: {livro.quantidade}")

livro.repor(5)
print(f"Quantidade atualizada: {livro.quantidade}")

livro.repor(-3)
print(f"Quantidade após tentativa inválida: {livro.quantidade}")