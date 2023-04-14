#Exercício 9 - Gravar um arquivo

#Pegue o código do exercício anterior e ao invés de imprimir os resultados na 
#tela, escreva-os em um arquivo txt. No seu código você pode deixar o nome do 
#arquivo hard-coded.


import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, "html.parser")

titulos = soup.find_all(class_="css-1qwxefa esl82me1")

with open("titulos_nytimes.txt", "w") as arquivo:
    for titulo in titulos:
        arquivo.write(titulo.text + "\n")
