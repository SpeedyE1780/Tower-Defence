from Enemies import *

class Buggy(Enemies):

    def __init__(Self,  path , Images):

        Enemies.__init__(Self , path , Images)

        Self.health = 250
        Self.speed = 8
        Self.score = 2


