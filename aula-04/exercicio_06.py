import random

numero_sorteado = random.randint(1, 5)

palpite = int(input("Adivinhe o número de 1 a 5: "))

if palpite == numero_sorteado:
    print("Parabéns! Você acertou!")    
else:
    print(f"Que pena! O número sorteado era {numero_sorteado}. Tente novamente!")