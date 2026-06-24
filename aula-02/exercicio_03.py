try:
    nota = float(input("Digite a nota do aluno: "))
except ValueError:
    print("Nota inválida! ")
else:
    print(f"A nota do aluno é: {nota:.1f}")