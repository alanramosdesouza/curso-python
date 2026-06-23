def calcular_total(preco, quantidade):
    total = preco * quantidade
    return total

resultado = calcular_total(10, 3)  
print(f"Total: R$ {resultado:.2f}")