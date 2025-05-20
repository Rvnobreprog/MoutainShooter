#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.enemy import Enemy
from Code.player import Player
import random

class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_Bg = []
                for i in range(7):
                    list_Bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_Bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
                return list_Bg

            case 'Player1':
                return Player('Player1',(10,WIN_HEIGHT/2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Enemy1':
                return Enemy('Enemy1',(WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT + 40 )))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT + 40 )))