def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    preco_final = preco - desconto
    return preco_final


resultado = calcular_desconto(100, 20)

print(f"Preço final: R$ {resultado:.2f}")