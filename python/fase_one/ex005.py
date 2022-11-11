n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# Para formatar a quantidade de casas --- {:.3f}

# Para não ocorre quebra de linha entre os print('') --- utilize (, end=' ')
# Quebrar linha no meio  \n

print('A soma é {}, \n o produto é {}, e a divisão é {:.3f}.'.format(s, m, d), end=' ')
print('Divisão inteira {}, e potência {}'.format(di, e))
