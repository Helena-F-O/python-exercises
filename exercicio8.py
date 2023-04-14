#Exercício 8

#Use os pacotes BeautifulSoup e requests para imprimir uma lista de todos 
#os títulos de artigos do New York Times.

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, "html.parser")

titulos = soup.find_all(class_="css-1qwxefa esl82me1")

for titulo in titulos:
    print(titulo.text)
