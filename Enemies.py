import pygame
pygame.init()
class Enemies:

    def __init__(Self , path , Images):
        
        Self.speed = 0
        Self.health = 0
        Self.path = path
        Self.x = path[0][0]
        Self.y = path[0][1]
        Self.current = 0
        Self.left = Images[0]
        Self.right = Images[1]
        Self.up = Images[2]
        Self.down = Images[3]
        Self.image = Self.right
        Self.doubledamage = False
        Self.counter = 0
        Self.timer = 0
        Self.score = 0

    def Update(Self):

        if Self.doubledamage:
            Self.counter += 1
            if Self.counter == Self.timer:
                Self.slowdown = False
                Self.counter = 0

        ##If arrived to target
        if Self.current < len(Self.path) - 2:
            if Self.x == Self.path[Self.current + 1][0] and Self.y == Self.path[Self.current + 1][1]:
                Self.current += 1


        ##Moving on y
        if Self.path[Self.current + 1][0] - Self.path[Self.current][0] == 0 and not Self.path[Self.current + 1][1] - Self.path[Self.current][1] == 0:

            ##Up
            if Self.path[Self.current + 1][1] - Self.path[Self.current][1] < 0:
                Self.image = Self.up
                Self.y -= Self.speed

            ##Down
            else:
                Self.image = Self.down
                Self.y += Self.speed

        ##Moving on x
        if Self.path[Self.current + 1][1] - Self.path[Self.current][1] == 0 and not Self.path[Self.current + 1][0] - Self.path[Self.current][0] == 0:

            ##Moving on the left
            if Self.path[Self.current + 1][0] - Self.path[Self.current][0] < 0:
                Self.image = Self.left
                Self.x -= Self.speed

            ##Moving on the right
            else:
                Self.image = Self.right
                Self.x += Self.speed
    def TakeDamage(Self , Damage):

        if Damage > 0:
            if Self.doubledamage:
                Self.health -= Damage * 2

            else:
                Self.health -= Damage

        else:

            Self.doubledamage = True
            Self.counter = 0

            if Damage == -1:
                Self.timer = 30

            elif Damage == -2:
                Self.timer = 60

            else:
                Self.timer = 90
        
