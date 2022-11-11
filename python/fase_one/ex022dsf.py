''' Crie um programa que leia o nome completo de uma pessoa e mostre:
 * O nome com todas as letras maiúsculas e minúsculas.
 * Quantas letras ao todo (sem considerar espaços)
 * Quantas letras tem o primeiro nome.  '''

# .strip()    - retorna a string resultante após a remoção do início e do final da string s de
# todos os caracteres em BRANCO

nome = str(input('Digite um nome completo: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo,  {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))