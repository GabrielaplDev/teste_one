nome = str(input('Qual é o seu nome? '))
# {:20} --- Adicionar 20 espaços
# {:>20} --- Adicionar espaço e alinhar a direita ou esquerda {:<20} / Para centralizar {^20}
# {=^20} para centralizar (nome) entre os caracateres = / =====Nome=====!
print('Prazer em te conhecer {:=^40}!'.format(nome))