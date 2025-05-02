#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Code.Const import WIN_WIDTH, WIN_WEIGHT
from Code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_WEIGHT))

    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass


            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit() # Close Window
            #         quit() # End pygame
