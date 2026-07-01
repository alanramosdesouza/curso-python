import calculos, situacao

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calculos.calcular_media(nota1, nota2)
resultado = situacao.verificar_situacao(media)

print(f"A média das notas é: {media}")
print(f"A situação do aluno é: {resultado}")