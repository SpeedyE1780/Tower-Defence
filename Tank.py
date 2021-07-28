from Enemies import *

class Tank(Enemies):

    def __init__(Self,  path , Images):

        Enemies.__init__(Self , path , Images)

        Self.health = 500
        Self.speed = 1
        Self.score = 10
