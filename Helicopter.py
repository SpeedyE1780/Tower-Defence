from Enemies import *
class Helicopter(Enemies):

    def __init__(Self,  path , Images):

        Enemies.__init__(Self , path , Images)
        
        Self.health = 100
        Self.speed = 10
        Self.score = 5
