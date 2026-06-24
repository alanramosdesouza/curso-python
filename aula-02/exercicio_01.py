try:
    preco = float(input("Digite o preço do produto: "))
    print(f'O preço do produto é: R$ {preco:.2f}')
except ValueError:
    print("Preço inválido.")