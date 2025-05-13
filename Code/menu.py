#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_YELLOW, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('../Assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option: int = 0
        pygame.mixer_music.load('../Assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #DRAW IMAGES(DESENHANDO OS TEXTOS COMO IMAGENS)
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text='MOUNTAIN', text_color =(255, 128, 0) , text_center_pos=((WIN_WIDTH/2),70))
            self.menu_text(text_size=50, text='BATTLE', text_color = (255, 128, 0),text_center_pos=((WIN_WIDTH / 2),120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_YELLOW,
                                   text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_WHITE,
                                   text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all events. INTERATIVIDADE
            for event in pygame.event.get(): #é uma função do Pygame que coleta todos os eventos que estão na fila de eventos.
                                             #Isso inclui: Teclas pressionadas, Cliques do mouse,Fechamento da janela..etc
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN: #desce menu via teclado
                    if event.key == pygame.K_DOWN: #verifica KEY DOWN, tecla para baixo.
                        if menu_option < len(MENU_OPTION) - 1: #pecorrer o teclado, pelo tamanho do menu(opcoes)
                            menu_option += 1 #cada vez que aperta, desce mais 1.
                        else:
                            menu_option=0 #apos chegar na ultima opção, volta para cima.

                    if event.key == pygame.K_UP: #verifica UP KEY, tecla para CIMA.
                        if menu_option > 0 : #pecorrer o teclado, pelo tamanho do menu(opcoes)
                            menu_option -= 1 #cada vez que aperta, SOBE mais 1. POR ISSO O SINAL DE '-'.
                        else:
                            menu_option= len(MENU_OPTION) - 1 #apos chegar na PRIMEIRA opção, volta para BAIXO.
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION [menu_option]





    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)


