# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o sálario do funcionario, salario R$: '))
#soma = salario * 0.15
#nvSalario = salario + soma

# 2° forma

soma = salario + (salario * 15 / 100)

print('O salario R${:.2f} com reajuste de 15% sera de R${:.2f}' .format(salario, soma))
