''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
 nome deles e escrevendo o nome do escolhido  '''

# Randomizador
from random import choice

a1 = str(input('Primeiro Nome do aluno: '))
a2 = str(input('Segundo Nome do aluno: '))
a3 = str(input('Terceiro Nome do aluno: '))
a4 = str(input('Quarto Nome do aluno: '))

# lista
lista = [a1, a2, a3, a4]

# Uma escolha dentro da lista
escolhido = choice(lista)

print('{}'.format(escolhido)