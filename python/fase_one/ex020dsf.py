''' O mesmo professor do desafio anterior quer sorteara ordem de aprensentção de trabalhos
dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada. '''

import random
g1 = str(input('Nome aluno 1: '))
g2 = str(input('Nome aluno 2: '))
g3 = str(input('Nome aluno 3: '))
g4 = str(input('Nome aluno 4: '))

lista = [g1, g2, g3, g4]
random.shuffle(lista)



print(lista)
