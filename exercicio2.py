#Exercício 2 - Palíndromos
#Peça uma string qualquer ao usuário e informe a ele se a string é um 
#palíndromo ou não. (um palíndromo é uma string que pode ser lida da mesma 
#forma, da esquerda para a direita ou vice-versa. Ex.: omo).

string = input("Digite uma palavra ou frase: ")

string = string.replace(" ", "").lower()

if string == string[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
