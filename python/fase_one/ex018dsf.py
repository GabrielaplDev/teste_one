''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo '''

from math import radians, sin, tan

an = float(input('Digite um angulo: '))

sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))


print('Seno = {:.2f}\nCosseno = {:.2f} \nTangente = {:.2f}'.format(sen, cos, tan))