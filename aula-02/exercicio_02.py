while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
        break

    except ValueError:
        print("Digite números inteiros válidos.")

    except ZeroDivisionError:
        print("Não é possível dividir por zero.")