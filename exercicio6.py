#Exercício 6 - Gerador de Senhas

#Escreva um gerador de senhas em python. Seja criativo com a forma de gerar 
#senhas - senhas fortes possuem uma mistura de letras minúsculas, maiúsculas, 
#números e símbolos. As senhas devem ser aleatórioas, gerando uma nova senha a 
#cada vez que o usuário executar o programa.

import random
import string

def gerar_senha(tamanho=12):
    
    letras_min = string.ascii_lowercase
    letras_mai = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation


    todos_caracteres = letras_min + letras_mai + digitos + simbolos


    senha = ''.join(random.sample(todos_caracteres, tamanho))
    return senha

nova_senha = gerar_senha()
print(nova_senha)
