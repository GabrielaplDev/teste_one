''' Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. '''

import pygame

pygame.mixer.init() # Para iniciar o uso da biblioteca
pygame.init()

pygame.mixer.music.load('ex21.mp3')  #
pygame.mixer.music.play()
pygame.event.wait()  # Espera a musica terminar para encerrar o progama
