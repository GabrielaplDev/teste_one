# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua aréa e a quantidade de tinta necessaria
#para pinta-la, sabendo que cada lata de tinta, pinta uma área de 2m².

larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m² '.format(larg, alt, area))
print('Para pintar essa parede sera necessario {} litro(S) de tinta'.format(tinta))