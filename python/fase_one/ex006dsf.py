# Crie um algoritimo que leia e mostre o seu dobro, triplo e raiz quadrada
import math

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = math.sqrt(n)   # ou: r = n ** (1/2)

print('O número digitado é {}, segue os valores a baixo: \nO dobro é {}, o triplo é {}, é a raiz quadra é {:.2f}'.format(n, d, t, r))
