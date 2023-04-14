#Exercício 4 - Jogo da adivinhação

#Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). Peça ao usuário para 
#adivinhar o número, e então diga se a tentativa foi menor, maior ou correta. 
#(Dica: lembre-se de usar o input dos exercícios anteriores). Mantenha o jogo 
#executando até que o usuário digite "sair".

import random

while True:
    
    numero = random.randint(1, 9)
    
    tentativa = input("Adivinhe o número entre 1 e 9 (ou digite 'sair' para sair): ")
    
    if tentativa == "sair":
        break
        
    tentativa = int(tentativa)
    
    if tentativa < numero:
        print("Tentativa menor que o número!")
    elif tentativa > numero:
        print("Tentativa maior que o número!")
    else:
        print("Parabéns! Você acertou o número!")
