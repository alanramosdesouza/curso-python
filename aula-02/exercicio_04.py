try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Número inválido! ")
else:
    print(f"O número digitado é: {numero}")
finally:
    print('Programa finalizado.10')