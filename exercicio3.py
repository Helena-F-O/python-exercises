#Exercício 3 - Pedra, Papel, Tesoura

#Faça um jogo de pedra, papel ou tesoura de dois jogadores. 
#(Dica: peça as jogadas ao usuário - usando input - compare-os, 
#imprima uma mensagem parabenizando o vencedor e pergunte ao usuário se 
#quer continuar jogando).

#Lembrando as regras:

#Pedra vence tesoura
#Tesoura vence papel
#Papel vence pedra


def determinar_vencedor(jogada1, jogada2):
    if jogada1 == jogada2:
        return None
    elif jogada1 == "pedra" and jogada2 == "tesoura":
        return "jogador 1"
    elif jogada1 == "tesoura" and jogada2 == "papel":
        return "jogador 1"
    elif jogada1 == "papel" and jogada2 == "pedra":
        return "jogador 1"
    else:
        return "jogador 2"


continuar = True

while continuar:
    jogada1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
    jogada2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

    vencedor = determinar_vencedor(jogada1, jogada2)

    if vencedor is None:
        print("Empate!")
    else:
        print(f"{vencedor.capitalize()} venceu!")

    resposta = input("Quer jogar novamente? (sim ou não): ").lower()
    while resposta not in ["sim", "não"]:
        resposta = input("Resposta inválida. Quer jogar novamente? (sim ou não): ").lower()
    if resposta == "não":
        continuar = False
