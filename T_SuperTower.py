import pygame
import math
from Tower import *

pygame.init()
class T_SuperTower(Tower):

    def __init__(Self , sc , Images):

        Self.L1 = Images  
        Self.image = Self.L1[0]
        Self.level = 5
        Self.range = 100
        Self.damage = 100
        Self.x = 0
        Self.y = 0
        Self.bulletx = 0
        Self.bullety = 0
        Self.angle = 0
        Self.cooldown = 0
        Self.screen = sc
        Self.target = 0
        Self.reset = 120
        Self.color = (255 , 0 , 0)


   
