''' Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
 Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6 '''
import math   # Ou // from math import trunc

''' 1° maneira // num = float(input('Digite um valor: '))
  print('{:.0f} ' .format(num))  '''

# 2° forma

num = float(input('Digte um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num))) #  .format(num,trunc(num)))

''' 3° forma, ao invez de utilizar import math, pode-se utilizar uma função interna 
 .format(num, int(num))
'''