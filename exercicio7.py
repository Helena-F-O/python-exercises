#Exercício 7 - Leitura de arquivos

#Dado um arquivo .txt que contem uma lista de nomes, conte quantas vezes cada 
#nome aparece no arquivo e imprima os resultados na tela. Um arquivo nomes.txt 
#é fornecido junto a esse repositório.

nome_arquivo = "names.txt"
contagem_nomes = {}

with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        nome = linha.strip()
        if nome in contagem_nomes:
            contagem_nomes[nome] += 1
        else:
            contagem_nomes[nome] = 1

for nome, contagem in contagem_nomes.items():
    print(nome + ": " + str(contagem))
