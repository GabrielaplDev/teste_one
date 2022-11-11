# Escreva um programa que lçeia um valor em metros e o exiba convertido em centimetros e milímetros

print('Digite um valor a baixo em metros, para que seja convertido em centimetros e milimetros:  ')
n = float(input('Uma distancia em metros: '))
cm = n * 100
mm = n * 1000
print('A media de {} corresponde a {:.0f} cm e {:.0f} mm'.format(n, cm , mm))
