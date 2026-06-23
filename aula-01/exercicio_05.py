def verificar_situacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

nota = float(input("Digite a nota do aluno: "))
situacao = verificar_situacao(nota)
print(f"Situação do aluno: {situacao}")