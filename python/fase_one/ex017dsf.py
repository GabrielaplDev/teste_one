''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre
    o comprimento da hipotenusa. '''

'''  1° forma
 
co = float(input('Comprimento do cateto posto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}' .format(hi))

'''

''' 2° forma - Utilizando bibliotecas'''

from math import hypot

co = float(input('Comprimento do cateto posto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('{:.2f}' . format(hi))