# Faça um algoritimo que tramforme o real em dolar
# Considere US$ 1.00 = R$ 3.27

n = float(input('Digite o valor em R$ a ser convertido em US$. R$: '))

dolar = n / 3.27

print('Com R$ {:.2f} você pode comprar US${:.2f} '.format(n, dolar))