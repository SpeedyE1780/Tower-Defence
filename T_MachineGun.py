import pygame
import math
from Tower import *
pygame.init()
class T_MachineGun(Tower):

    def __init__(Self , sc , Images):

        Self.L1 = Images[0]
        Self.L2 = Images[1]
        Self.L3 = Images[2]  
        Self.image = Self.L1[0]
        Self.level = 1
        Self.range = 60
        Self.damage = 5
        Self.x = 0
        Self.y = 0
        Self.bulletx = 0
        Self.bullety = 0
        Self.angle = 0
        Self.cooldown = 0
        Self.reset = 5
        Self.target = 0
        Self.screen = sc
        Self.color = (0 , 0 , 255)
