#    Escreva um programa que gere uma senha aleatória com um determinado comprimento. A senha deve conter uma mistura de letras, números e caracteres especiais. O comprimento da senha deve ser fornecido pelo usuário. Se o comprimento for menor que 4, imprima uma mensagem de erro e peça ao usuário para fornecer um novo comprimento.
#    A senha deve ser aleatória, então cada vez que o usuário executar o programa, uma nova senha deve ser gerada. Obrigatoriamente, a senha deve conter pelo menos uma letra, um número e um caractere especial. A senha não pode conter espaços em branco.
#    O programa deve conter uma função chamada `gerar_senha` que recebe o comprimento da senha como parâmetro e retorna a senha gerada. Se o comprimento for inválido, a função deve retornar None.
#    Exemplo de saída:
#    - Dica: use a biblioteca random e a função shuffle para embaralhar os caracteres da senha.
#    - Dica: use a função choice, dessa mesma biblioteca, para escolher um caractere aleatório de uma string.
#    - Dica: use a biblioteca string para obter uma lista de caracteres válidos para a senha.

import string
import random
def gerar_senha(tamanho):
   if tamanho < 4:
      print("O tamanho da senha deve ser de pelo menos 4")
   elif tamanho > 20:
       print("A senha deverá ter até um limite de 15 caracteres")
   else:
      senha = [
          random.choice(string.ascii_letters),
          random.choice(string.digits),
          random.choice(string.punctuation),
        ]
      possibilidades = ''.join([string.ascii_letters, string.digits, string.punctuation])
      senha.extend(random.choices(possibilidades, k=tamanho-3))

      random.shuffle(senha)

      return ''.join(senha)

tamanho = int(input("Digite o comprimento da senha: "))

print(gerar_senha(tamanho))