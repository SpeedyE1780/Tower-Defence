import pygame
import math
from Tower import *
pygame.init()
class T_EMP(Tower):

    def __init__(Self , sc , Images):

        Self.L1 = Images[0]
        Self.L2 = Images[1]
        Self.L3 = Images[2]
        Self.image = Self.L1
        Self.level = 1
        Self.range = 60
        Self.damage = -1
        Self.x = 0
        Self.y = 0
        Self.bulletx = 0
        Self.bullety = 0
        Self.cooldown = 0
        Self.reset = 5
        Self.screen = sc
        Self.target = 0
        Self.color = (0 , 255 , 255)

    def Upgrade(Self):
        
        if Self.level == 1:

            Self.level = 2
            Self.image = Self.L2
            Self.damage = - 2
            Self.range += 5 * Self.level

        elif Self.level == 2:

            Self.level = 3
            Self.image = Self.L3
            Self.damage = - 3
            Self.range += 5 * Self.level
            
    def LookAt(Self , enemy):

        if Self.cooldown == 0:

                Self.distance = math.sqrt(math.pow((Self.x - enemy.x) , 2)+ math.pow((Self.y - enemy.y),2))
                if Self.distance <= Self.range:

                    Tower.Shoot(Self , enemy)
