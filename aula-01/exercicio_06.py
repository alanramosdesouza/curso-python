def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")