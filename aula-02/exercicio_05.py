def calcular_media(n1, n2):
           return (n1 + n2) / 2

def verificar_aprovacao(media):
                if media >= 7:
                    return "Aprovado"
                elif media >= 5:
                    return "Recuperação"
                else:
                    return "Reprovado"
                

while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            media = calcular_media(nota1, nota2)
            resultado = verificar_aprovacao(media)
            print(f"Média: {media:.2f} - Resultado: {resultado}")
            break
        else:
            print("As notas devem estar entre 0 e 10. Tente novamente.")
    except ValueError:
        print('Digite apenas números.')
    finally:
        print('Tentativa finalizada.')