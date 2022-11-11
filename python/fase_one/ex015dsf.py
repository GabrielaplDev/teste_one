# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e RS$0.15 por Km rodado

diasAluguel = int(input('O carro foi alugado por quantos dias? '))
kmRodados = float(input('O carro rodou por quantos Kms? '))

valorAluguel = float(diasAluguel * 60) + (kmRodados * 0.15)

print('O valor do aluguel é de: RS${:.2F}'.format(valorAluguel))


