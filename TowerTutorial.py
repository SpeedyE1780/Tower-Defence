import pygame
import math
pygame.init()

class TowerTutorial(pygame.sprite.Sprite):

    def __init__(Self):

        Self.image = pygame.image.load("Media/Towers/Machine_Gun/L1 Images/L1_MachineGun0000.tif").convert_alpha()
        Self.level = 1
        Self.range = 40
        Self.damage = 20
        Self.visible = False
        Self.cooldown = 0
        
        

    def coordinates(Self , x , y):
        Self.x = x
        Self.y = y
        Self.bulletx = x + 20
        Self.bullety = y + 20

    def showrange(Self , screen):

        Self.visible = True
        pygame.draw.circle(screen , ( 255 , 255 ,255) ,[Self.x + 20 , Self.y + 20]  , Self.range , 2)

    def lookat(Self , enemy):

        tevector = ((enemy.x -Self.x) , (enemy.y - Self.y))

        tedistance = math.sqrt(math.pow(tevector[0] , 2) + math.pow(tevector[1] , 2))

        coste = -tevector[0] / tedistance

        angle = int(math.degrees(math.acos(coste)))

        if angle > 10 and angle < 100:
            angle = "0" + str(angle)
        elif angle < 10:
            angle = "00" + str(angle)

        file = "Media/Towers/Machine_Gun/L1 Images/L1_MachineGun0" + str(angle) + ".tif"
        Self.image = pygame.image.load(file).convert_alpha()
        
    def upgrade(Self):

        if Self.visible:

            if Self.level == 1:
                Self.image = pygame.image.load("Media/Towers/Machine_Gun/L2 Images/L2_MachineGun0000.tif").convert_alpha()
                Self.level += 1
                Self.range = 50
                Self.damage = 40

            elif Self.level == 2:
                Self.image = pygame.image.load("Media/Towers/Machine_Gun/L3 Images/L3_Machine_Gun0000.tif").convert_alpha()
                Self.level += 1
                Self.range = 70
                Self.damage = 60

    def shoot(Self , enemy , screen):

        if Self.cooldown == 0:
            distance = math.sqrt(math.pow((Self.x - enemy.x) , 2)+ math.pow((Self.y - enemy.y),2))
            
            if distance <= Self.range:
                
                bulletdistance = math.sqrt(math.pow((Self.bulletx - enemy.x - 20) , 2)+ math.pow((Self.bullety - enemy.y - 20),2))
                btdistance =  math.sqrt(math.pow((Self.bulletx - Self.x - 20) , 2)+ math.pow((Self.bullety - Self.y - 20),2))

                if bulletdistance < 20:
                    Self.bulletx = Self.x + 20
                    Self.bullety = Self.y + 20
                    enemy.TakeDamage(Self.damage)
                    Self.cooldown += 1

                if btdistance > distance:

                    Self.bulletx = enemy.x + 20
                    Self.bullety = enemy.y + 20
                    enemy.TakeDamage(Self.damage)
                    
                
                    
                pygame.draw.circle(screen , (255 , 255 , 0) , [Self.bulletx , Self.bullety] , 7)

                directionx = (enemy.x + 20 - Self.bulletx) / bulletdistance
                directiony = (enemy.y + 20 - Self.bullety) / bulletdistance

                Self.bulletx += int(directionx * 10)
                Self.bullety += int(directiony * 10)

        else:
            Self.cooldown += 1
       

        if Self.cooldown == 5:
            Self.cooldown =0
        

        
        

        

        
