''' Crie um programa que lçeia o nome de uma cidade e diga se ela começã ou não com o nome "SANTO" '''

cidade = str(input('Em que cidade você nasceu ? ' )).strip() #elimina espaçõs
print(cidade[:5].upper() == 'SANTO')