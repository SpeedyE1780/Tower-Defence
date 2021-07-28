import pygame
pygame.init()

class EnemyTutorial(pygame.sprite.Sprite):

    def __init__(Self , x , y):

        pygame.sprite.Sprite.__init__(Self)
        Self.speed = 4
        Self.health = 100
        Self.image = pygame.image.load("Media/Units/Buggy/Images/Buggy_Right.tif").convert_alpha()
        Self.rect = Self.image.get_rect()
        Self.x = x
        Self.y = y

        Self.avoiding = False
        Self.towerx = 0
        Self.towery = 0

    def update(Self):

        if Self.avoiding:
            
            if int(Self.x/40) == int(Self.towerx/40) - 1 and int(Self.y/40) == int(Self.towery/40):

                Self.y += Self.speed
                Self.image = pygame.image.load("Media/Units/Buggy/Images/Buggy_Down.tif").convert_alpha()

            elif int(Self.x/40) == int(Self.towerx/40) + 1 and not Self.y == Self.towery:

                Self.y -= Self.speed
                Self.image = pygame.image.load("Media/Units/Buggy/Images/Buggy_Up.tif").convert_alpha()

            else:
            
                Self.x += Self.speed
                Self.image = pygame.image.load("Media/Units/Buggy/Images/Buggy_Right.tif").convert_alpha()
            

        else:
            
            Self.x += Self.speed
            Self.image = pygame.image.load("Media/Units/Buggy/Images/Buggy_Right.tif").convert_alpha()

    def avoid(Self , tx , ty):
        Self.avoiding = True
        Self.towerx = tx
        Self.towery = ty

    def TakeDamage(Self , damage):

        Self.health -= damage
            
        
