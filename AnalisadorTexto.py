#Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras (independentemente se há repetição ou não), a quantidade de cada palavra e a quantidade de cada letra.
#Ignore maiúsculas e minúsculas ao contar letras (ou seja, transforme tudo para minúsculas).
#Faça o devido tratamento para pontuação e espaços ao contar palavras.
#O programa deve conter uma função chamada `analisar_texto` que recebe o texto como parâmetro e retorna a contagem de palavras, a frequência de palavras e a frequência de letras.
#A função deve ser devidamente documentada.
#   Dica: use o módulo `string` para obter uma lista de caracteres de pontuação. Exemplo:

""""
import string
print(string.punctuation)
#   Dica: use o módulo `collections` para obter um contador de palavras e letras. Exemplo:
from collections import Counter
print(Counter(['a', 'b', 'a', 'c', 'b', 'a']))
print(Counter('abacba'))
"""

import string
from collections import Counter

def analisar_texto(texto):
# Analisa o texto fornecido e calcula a contagem de palavras, a frequência de palavras e a frequência de letras do texto a ser analisado
# Contagem de palavras, frequência de palavras e frequência de letras
# Remove a pontuação do texto
        tratamento = str.maketrans('', '', string.punctuation)
        texto_tratado = texto.translate(tratamento)
        palavras = texto_tratado.split()
        contagem_palavras = len(palavras)
        frequencia_palavras = Counter(palavras)
        # Converte o texto para minúsculas e conta a frequência das letras
        frequencia_letras = Counter(texto_tratado.lower())

        return contagem_palavras, frequencia_palavras, frequencia_letras

texto = input("TEXTO:")

contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)

print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")