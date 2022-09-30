'Faça um programa em python que abra e reproduza o áudio de um arquivo mp3'
import pygame
musica = 'ex021.mp3'
pygame.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
pygame.event.wait()
