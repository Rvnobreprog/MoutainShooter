#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.Background import Background
from Code.Const import WIN_WIDTH


class EntityFactory:

    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_Bg = []
                for i in range(7):
                    list_Bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_Bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
        return list_Bg
