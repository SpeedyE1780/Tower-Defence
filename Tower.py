import pygame
import math
pygame.init()
class Tower:

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
        Self.color = (255 , 255 , 255)

    def Update(Self , EnemiesList):

        if Self.target == 0:
            
            for enemy in EnemiesList:
                if enemy.health > 0 and enemy.x >= 40:
                    Self.distance = math.sqrt(math.pow((Self.x - enemy.x) , 2)+ math.pow((Self.y - enemy.y),2))
                    if Self.distance <= Self.range:
                        if Self.target == 0:
                            Self.target = enemy
                            Self.LookAt(Self.target)
                        
        else:

            Self.distance = math.sqrt(math.pow((Self.x - Self.target.x) , 2)+ math.pow((Self.y - Self.target.y),2))

            if Self.distance > Self.range or Self.target.health <= 0 or Self.target.x > 600:
                Self.target = 0
                Self.bulletx = Self.x + 20
                Self.bullety = Self.y + 20

            else:

                Self.LookAt(Self.target)

        if not Self.cooldown == 0:
            Self.cooldown += 1

        if Self.cooldown == Self.reset:

            Self.cooldown = 0

    def SetCoordinates(Self , x , y):

        Self.x = x
        Self.bulletx = x + 20

        Self.y = y
        Self.bullety = y + 20
        
        
    def ShowRange(Self):

        pygame.draw.circle(Self.screen , (255 , 255 , 255) , [Self.x + 20 , Self.y + 20] , Self.range , 2)

    def LookAt(Self , enemy):

        T2EVector = ((enemy.x - Self.x) , (enemy.y - Self.y))

        T2EDistance = math.sqrt(math.pow(T2EVector[0] , 2) + math.pow(T2EVector[1] , 2))

        if not T2EDistance == 0:
            cosT2E = -T2EVector[0] / T2EDistance

            Self.angle = int(math.degrees(math.acos(cosT2E)))

            if enemy.y < Self.y:
                Self.angle = 360 - Self.angle
                if Self.angle == 360:
                    Self.angle = 0

            if Self.level == 1 or Self.level == 5:

                Self.image = Self.L1[Self.angle]

            elif Self.level == 2:

                Self.image = Self.L2[Self.angle]

            elif Self.level == 3:

                Self.image = Self.L3[Self.angle]


            if Self.cooldown == 0:

                Self.distance = math.sqrt(math.pow((Self.x - enemy.x) , 2)+ math.pow((Self.y - enemy.y),2))
                if Self.distance <= Self.range:

                    Self.Shoot(enemy)

    def Upgrade(Self):

        if Self.level == 1:

            Self.level = 2
            Self.image = Self.L2[0]
            Self.damage += 10 * Self.level
            Self.range += 5 * Self.level

        elif Self.level == 2:

            Self.level = 3
            Self.image = Self.L3[0]
            Self.damage += 10 * Self.level
            Self.range += 5 * Self.level

    def Shoot(Self , enemy):

        draw = True
        bulletdistance = math.sqrt(math.pow((Self.bulletx - enemy.x - 20) , 2)+ math.pow((Self.bullety - enemy.y - 20),2))
        btdistance =  math.sqrt(math.pow((Self.bulletx - Self.x - 20) , 2)+ math.pow((Self.bullety - Self.y - 20),2))

        if bulletdistance < 10:
            Self.bulletx = Self.x + 20
            Self.bullety = Self.y + 20
            draw = False
            enemy.TakeDamage(Self.damage)
            Self.cooldown += 1

        if btdistance > Self.distance:

            draw = False
            enemy.TakeDamage(Self.damage)
            Self.cooldown += 1
            Self.bulletx = Self.x + 20
            Self.bullety = Self.y + 20
            
        
        if draw:  
            pygame.draw.circle(Self.screen , Self.color , [Self.bulletx , Self.bullety] , 5)

        if not bulletdistance == 0:
            directionx = (enemy.x + 20 - Self.bulletx) / bulletdistance
            directiony = (enemy.y + 20 - Self.bullety) / bulletdistance

            Self.bulletx += int(directionx * 10)
            Self.bullety += int(directiony * 10)
        
