import pygame ,sys
from pygame.locals import *
from Enemies import *
from Tank import *
from Buggy import *
from Helicopter import *
from EnemyTutorial import *
from TowerTutorial import *
from Tower import *
from T_MachineGun import *
from T_EMP import *
from T_Laser import *
from T_Rocket import *
from T_SuperTower import *
from Node import *
import random

pygame.init()
resolution = (640 , 480)
black = (0 , 0 ,0)
white = (255 , 255 , 255)
gray = (128 , 128 , 128)
screen = pygame.display.set_mode(resolution)
screen.fill(black)

"""
State = 0 Main Menu
State = 1.1 Help Page 1
State = 1.2 Help Page 2
State = 2 Tutorial
State = 3 Game
"""
State = 0

Running = True

Loading = pygame.font.Font(None , 160).render("LOADING" , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()

##Load Images
BG = pygame.image.load("Media/Background.jpg").convert()
floor = pygame.image.load("Media/metalFloor.jpg").convert()

pygame.mixer.music.load("Media/BG_Music.wav")
Music = False

screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING." , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()

##Tower Icons

##Machine Gun
MachineGunico = pygame.image.load("Media/Towers/Machine_Gun/Help/L1.tif").convert_alpha()
MachineGunico2 = pygame.image.load("Media/Towers/Machine_Gun/Help/L2.tif").convert_alpha()
MachineGunico3 = pygame.image.load("Media/Towers/Machine_Gun/Help/L3.tif").convert_alpha()

##EMP
EMPico = pygame.image.load("Media/Towers/EMP/Help/L1.tif").convert_alpha()
EMPico2 = pygame.image.load("Media/Towers/EMP/Help/L2.tif").convert_alpha()
EMPico3 = pygame.image.load("Media/Towers/EMP/Help/L3.tif").convert_alpha()

##Laser
Laserico = pygame.image.load("Media/Towers/Laser/Help/L1.tif").convert_alpha()
Laserico2 = pygame.image.load("Media/Towers/Laser/Help/L2.tif").convert_alpha()
Laserico3 = pygame.image.load("Media/Towers/Laser/Help/L3.tif").convert_alpha()

##Rocket
Rocketico = pygame.image.load("Media/Towers/Rocket/Help/L1.tif").convert_alpha()
Rocketico2 = pygame.image.load("Media/Towers/Rocket/Help/L2.tif").convert_alpha()
Rocketico3 = pygame.image.load("Media/Towers/Rocket/Help/L3.tif").convert_alpha()

##SuperTower
SuperTowerico = pygame.image.load("Media/Towers/Super_Tower/Help/Help.tif").convert_alpha()


screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING.." , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()


##Tower Images
##Machine Gun
MG_L1 =[]
MG_L2 = []
MG_L3 = []
for i in range(0 , 360):
    L1_path = "Media/Towers/Machine_Gun/L1 Images/L1_MachineGun0"
    L2_path = "Media/Towers/Machine_Gun/L2 Images/L2_MachineGun0"
    L3_path = "Media/Towers/Machine_Gun/L3 Images/L3_Machine_Gun0"
    if i > 9 and i < 100:

        L1_path += "0" + str(i) + ".tif"
        L2_path += "0" + str(i) + ".tif"
        L3_path += "0" + str(i) + ".tif"

    elif i < 10:

        L1_path += "00" + str(i) + ".tif"
        L2_path += "00" + str(i) + ".tif"
        L3_path += "00" + str(i) + ".tif"

    else:

        L1_path += str(i) + ".tif"
        L2_path += str(i) + ".tif"
        L3_path += str(i) + ".tif"
      
    MG_L1.append(pygame.image.load(L1_path).convert_alpha())
    MG_L2.append(pygame.image.load(L2_path).convert_alpha())
    MG_L3.append(pygame.image.load(L3_path).convert_alpha())

MG = [MG_L1 , MG_L2 , MG_L3]


screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING.." , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()


##EMP
EMP_L1 = pygame.image.load("Media/Towers/EMP/L1/L1.tif").convert_alpha()
EMP_L2 = pygame.image.load("Media/Towers/EMP/L2/L2.tif").convert_alpha()
EMP_L3 = pygame.image.load("Media/Towers/EMP/L3/L3.tif").convert_alpha()

EMP = [EMP_L1 , EMP_L2 , EMP_L3]


screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING..." , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()


##Laser
Laser_L1 =[]
Laser_L2 = []
Laser_L3 = []
for i in range(0 , 360):
    L1_path = "Media/Towers/Laser/L1 Images/L1_Laser0"
    L2_path = "Media/Towers/Laser/L2 Images/L2_Laser0"
    L3_path = "Media/Towers/Laser/L3 Images/L3_Laser0"
    if i > 9 and i < 100:

        L1_path += "0" + str(i) + ".tif"
        L2_path += "0" + str(i) + ".tif"
        L3_path += "0" + str(i) + ".tif"

    elif i < 10:

        L1_path += "00" + str(i) + ".tif"
        L2_path += "00" + str(i) + ".tif"
        L3_path += "00" + str(i) + ".tif"

    else:

        L1_path += str(i) + ".tif"
        L2_path += str(i) + ".tif"
        L3_path += str(i) + ".tif"
      
    Laser_L1.append(pygame.image.load(L1_path).convert_alpha())
    Laser_L2.append(pygame.image.load(L2_path).convert_alpha())
    Laser_L3.append(pygame.image.load(L3_path).convert_alpha())

Laser = [Laser_L1 , Laser_L2 , Laser_L3]


screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING" , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()


##Rocket
Rocket_L1 =[]
Rocket_L2 = []
Rocket_L3 = []
for i in range(0 , 360):
    L1_path = "Media/Towers/Rocket/L1 Images/L1_Rocket0"
    L2_path = "Media/Towers/Rocket/L2 Images/L2_Rocket0"
    L3_path = "Media/Towers/Rocket/L3 Images/L3_Rocket0"
    if i > 9 and i < 100:

        L1_path += "0" + str(i) + ".tif"
        L2_path += "0" + str(i) + ".tif"
        L3_path += "0" + str(i) + ".tif"

    elif i < 10:

        L1_path += "00" + str(i) + ".tif"
        L2_path += "00" + str(i) + ".tif"
        L3_path += "00" + str(i) + ".tif"

    else:

        L1_path += str(i) + ".tif"
        L2_path += str(i) + ".tif"
        L3_path += str(i) + ".tif"
      
    Rocket_L1.append(pygame.image.load(L1_path).convert_alpha())
    Rocket_L2.append(pygame.image.load(L2_path).convert_alpha())
    Rocket_L3.append(pygame.image.load(L3_path).convert_alpha())

Rocket = [Rocket_L1 , Rocket_L2 , Rocket_L3]

screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING." , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()

##Super Tower
SuperTower =[]
for i in range(0 , 360):
    L1_path = "Media/Towers/Super_Tower/Images/SuperTower0"
    if i > 9 and i < 100:

        L1_path += "0" + str(i) + ".tif"

    elif i < 10:

        L1_path += "00" + str(i) + ".tif"

    else:

        L1_path += str(i) + ".tif"
      
    SuperTower.append(pygame.image.load(L1_path).convert_alpha())

screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING.." , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()

##Gate Images
GateEntry = pygame.image.load("Media/Gates/Images/GateEntry.tif").convert_alpha()
GateExit = pygame.image.load("Media/Gates/Images/GateExit.tif").convert_alpha()


screen.fill(black)
Loading = pygame.font.Font(None , 160).render("LOADING..." , True , white)
screen.blit(Loading , [0 , 240])
pygame.display.update()
##Enemy Images

##Tank
TankImage = pygame.image.load("Media/Units/Tank/Images/Tank_Help.tif").convert_alpha()
TankLeft = pygame.image.load("Media/Units/Tank/Images/Tank_Left.tif").convert_alpha()
TankRight = pygame.image.load("Media/Units/Tank/Images/Tank_Right.tif").convert_alpha()
TankUp = pygame.image.load("Media/Units/Tank/Images/Tank_Up.tif").convert_alpha()
TankDown = pygame.image.load("Media/Units/Tank/Images/Tank_Down.tif").convert_alpha()
TankImages = [TankLeft , TankRight , TankUp , TankDown]

##Buggy
BuggyImage = pygame.image.load("Media/Units/Buggy/Images/Buggy_Help.tif").convert_alpha()
BuggyLeft = pygame.image.load("Media/Units/Buggy/Images/Buggy_Left.tif").convert_alpha()
BuggyRight = pygame.image.load("Media/Units/Buggy/Images/Buggy_Right.tif").convert_alpha()
BuggyUp = pygame.image.load("Media/Units/Buggy/Images/Buggy_Up.tif").convert_alpha()
BuggyDown = pygame.image.load("Media/Units/Buggy/Images/Buggy_Down.tif").convert_alpha()
BuggyImages = [BuggyLeft , BuggyRight , BuggyUp , BuggyDown]


##Helicopter
HelicopterImage = pygame.image.load("Media/Units/Helicopter/Images/Helicopter_Help.tif").convert_alpha()
HelicopterLeft = pygame.image.load("Media/Units/Helicopter/Images/Helicopter_Left.tif").convert_alpha()
HelicopterRight = pygame.image.load("Media/Units/Helicopter/Images/Helicopter_Right.tif").convert_alpha()
HelicopterUp = pygame.image.load("Media/Units/Helicopter/Images/Helicopter_Up.tif").convert_alpha()
HelicopterDown = pygame.image.load("Media/Units/Helicopter/Images/Helicopter_Down.tif").convert_alpha()
HelicopterImages = [HelicopterLeft , HelicopterRight , HelicopterUp , HelicopterDown]

screen.fill(black)
pygame.display.update()

##Track the progress of the tutorial
Stage = 0
tEnemy = []
tTower = []
tRow = 8
tColumn = 5 
visiblerange = 0
Tags = 0

##Play Variables
ArenaTiles = []
SelectedTower = 0
TowerType = 0
Life = 3
Waves = 1
WaveStarted = False
EnemySpawning = False
EnemyList = []
enemycount = 0
SpawnedEnemy = 0
Time = 0
TimeCounter = 0
Score = 0
PlacingTower = False
FinishedSpawning = False
Path = []
EnemySpawn = 30
EnemyKilled = 0

##Helicopter Path with no obstacle
HelicopterPath = []
for i in range(0 , 16):
    HelicopterPath.append([0])
    for j in range(0 , 10):
        HelicopterPath[i].append(0)

clock = pygame.time.Clock()
fps = 30

def astar(maze, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                x = current.position[0] * 40
                y = current.position[1] * 40 + 40
                path.append((x , y))
                current = current.parent
            Solution = path[::-1] # Return reversed path
            return Solution

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
            Add = True

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > 9 or node_position[1] < 0:
                Add = False

            if Add:
                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] != 0:
                    Add = False

            if Add:
                # Create new node
                new_node = Node(current_node, node_position)
                
                # Append
                children.append(new_node)

        # Loop through children
        for child in children:
            Add = True
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    Add = False

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    Add = False
            if Add:  
                # Add the child to the open list
                open_list.append(child)
                
    return False

while Running:

    clock.tick(fps)

    ##Main Menu
    if State == 0:

        ##Background
        screen.blit(BG , (0,0))

        ##Title
        Title_text = pygame.font.Font(None , 100).render("TOWER DEFENCE" , True , white)
        screen.blit(Title_text , [20 , 0])

        ##Play Button
        Play_Button = pygame.Surface([65 , 20])
        Play_Button.fill(gray)
        screen.blit(Play_Button , [500 , 320])
        play_text = pygame.font.Font(None , 32).render("PLAY!" , True , white)
        screen.blit(play_text , [500 , 320])

        ##Tutorial Button
        Help_Button = pygame.Surface([120 , 20])
        Help_Button.fill(gray)
        screen.blit(Help_Button , [500 , 360])
        Help_text = pygame.font.Font(None , 32).render("TUTORIAL!" , True , white)
        screen.blit(Help_text , [500 , 360])

        ##Help Button
        Help_Button = pygame.Surface([65 , 20])
        Help_Button.fill(gray)
        screen.blit(Help_Button , [500 , 400])
        Help_text = pygame.font.Font(None , 32).render("HELP!" , True , white)
        screen.blit(Help_text , [500 , 400])

        ##Quit Button
        Quit_Button = pygame.Surface([65 , 20])
        Quit_Button.fill(gray)
        screen.blit(Quit_Button , [500 , 440])
        Quit_text = pygame.font.Font(None , 32).render("QUIT!" , True , white)
        screen.blit(Quit_text , [500 , 440])

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                pt = pygame.mouse.get_pos()
                x , y = pt

                ##Play Button Clicked
                if x in range(500 , 566) and y in range(320 , 361):
                    screen.fill(black)
                    State = 3
                    Tags = 0
                    Life = 3
                    Waves = 1
                    WaveStarted = False
                    EnemySpawning = False
                    EnemyList = []
                    enemycount = 0
                    SpawnedEnemy = 0
                    Path = []
                    Time = 0
                    Score = 0
                    TimeCounter = 0
                    tRow = 8
                    tColumn = 5
                    PlacingTower = False
                    FinishedSpawning = False
                    EnemySpawn = 30
                    EnemyKilled = 0
                    
                    ##Initialize the map
                    for i in range(0 , 16):
                        ArenaTiles.append([0])
                        for j in range(0 , 10):
                            ArenaTiles[i].append(0)

                ##Tutorial Button Clicked
                if x in range(500 , 621) and y in range(360 , 401):
                    screen.fill(black)
                    State = 2
                    Stage = 0
                    tTower = []
                    tEnemy = []

                ##Help Button Clicked
                if x in range(500 , 566) and y in range(400 , 441):
                    screen.fill(black)
                    State = 1.1

                ##Quit Button Clicked
                if x in range(500 , 566) and y in range(440 , 481):
                    Running = False

            ##Escape is pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Running = False

                if event.key == K_m:
                        if not Music:
                            Music = True
                            pygame.mixer.music.play(-1)
                        else:
                            pygame.mixer.music.stop()
                            Music = False
                

            if event.type == QUIT:
                Running = False


    ##Help Page 1
    elif State == 1.1:

        ##Background
        screen.blit(BG , (0,0))

        ##Title
        Title_text = pygame.font.Font(None , 100).render("INSTRUCTIONS" , True , white)
        screen.blit(Title_text , [20 , 0])

        ##Instructions
        Instruction_text = pygame.font.Font(None , 32).render("Enemy units will enter the arena from a random gate" , True , white)
        screen.blit(Instruction_text , [0 , 75])

        Instruction_text = pygame.font.Font(None , 32).render("Enemy units will head towards a random gate" , True , white)
        screen.blit(Instruction_text , [0 , 100])

        Instruction_text = pygame.font.Font(None , 32).render("Create the longest path possible while adding towers" , True , white)
        screen.blit(Instruction_text , [0 , 125])

        Instruction_text = pygame.font.Font(None , 32).render("Helicopter will fly over the towers to reach the destination" , True , white)
        screen.blit(Instruction_text , [0 , 150])

        Instruction_text = pygame.font.Font(None , 32).render("Before every wave you have the chance to place your towers" , True , white)
        screen.blit(Instruction_text , [0 , 175])

        Instruction_text = pygame.font.Font(None , 32).render("You have 3 lives you lose once you run out of lives" , True , white)
        screen.blit(Instruction_text , [0 , 200])

        Instruction_text = pygame.font.Font(None , 32).render("Use the tags you get after each wave to upgrade your towers" , True , white)
        screen.blit(Instruction_text , [0 , 225])

        Instruction_text = pygame.font.Font(None , 32).render("Every 3 waves more helicopters will spawn" , True , white)
        screen.blit(Instruction_text , [0 , 250])

        Instruction_text = pygame.font.Font(None , 32).render("Every 5 waves more tanks will spawn" , True , white)
        screen.blit(Instruction_text , [0 , 275])

        Instruction_text = pygame.font.Font(None , 32).render("Press the escape button to go to the main menu" , True , white)
        screen.blit(Instruction_text , [0 , 300])

        Instruction_text = pygame.font.Font(None , 32).render("Press M to mute/unmute the game" , True , white)
        screen.blit(Instruction_text , [0 , 325])

        Instruction_text = pygame.font.Font(None , 32).render("Press P to pause the game" , True , white)
        screen.blit(Instruction_text , [0 , 350])

        Instruction_text = pygame.font.Font(None , 32).render("Press S to start the wave" , True , white)
        screen.blit(Instruction_text , [0 , 375])

        Instruction_text = pygame.font.Font(None , 32).render("Press < to speed down the game or > to speed up the game" , True , white)
        screen.blit(Instruction_text , [0 , 400])

        
        
        

        ##Next Button
        Next_Button = pygame.Surface([70 , 20])
        Next_Button.fill(gray)
        screen.blit(Next_Button , [550 , 440])
        Next_text = pygame.font.Font(None , 32).render("NEXT!" , True , white)
        screen.blit(Next_text , [550 , 440])
        
        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                
                pt = pygame.mouse.get_pos()
                x , y = pt
                
                ##Next Button Clicked
                if x in range(550 , 621) and y in range(440 , 461):
                    screen.fill(black)
                    State = 1.2

            ##Escape is pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    screen.fill(black)
                    State = 0

                if event.key == K_m:
                    if not Music:
                        Music = True
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
                        Music = False
                    
            if event.type == QUIT:
                
                screen.fill(black)
                State = 0

        
    ##Help Pages 2
    elif State == 1.2:
        
        ##Background
        screen.blit(BG , (0,0))

        ##Title
        Title_text = pygame.font.Font(None , 100).render("INSTRUCTIONS" , True , white)
        screen.blit(Title_text , [20 , 0])

        ##Instruction Text

        ##Enemies
        Instruction_text = pygame.font.Font(None , 32).render("Enemy Units:" , True , white)
        screen.blit(Instruction_text , [0 , 75])

        ##Tank
        Instruction_text = pygame.font.Font(None , 32).render("Tank: Slow but has high health" , True , white)
        screen.blit(Instruction_text , [60 , 110])
        screen.blit(TankImage , [0 , 100])

        ##Buggy
        Instruction_text = pygame.font.Font(None , 32).render("Buggy: Fast but has low health" , True , white)
        screen.blit(Instruction_text , [60 , 150])
        screen.blit(BuggyImage , [0 , 140])

        ##Helicopter
        Instruction_text = pygame.font.Font(None , 32).render("Helicopter: Meduim speed but flies over towers" , True , white)
        screen.blit(Instruction_text , [60 , 190])
        screen.blit(HelicopterImage , [0 , 180])                    

        
        ##Towers
        Instruction_text = pygame.font.Font(None , 32).render("Towers:" , True , white)
        screen.blit(Instruction_text , [0 , 230])
        
        ##Machine Gun
        Instruction_text = pygame.font.Font(None , 32).render("Machine Gun:" , True , white)
        screen.blit(Instruction_text , [0 , 260])
        screen.blit(MachineGunico , [150 , 250])
        screen.blit(MachineGunico2 , [190 , 250])
        screen.blit(MachineGunico3 , [230 , 245])
        Instruction_text = pygame.font.Font(None , 32).render("High fire rate but low damage" , True , white)
        screen.blit(Instruction_text , [270 , 260])
        
        ##EMP
        Instruction_text = pygame.font.Font(None , 32).render("EMP:" , True , white)
        screen.blit(Instruction_text , [0 , 290])
        screen.blit(EMPico , [60 , 280])
        screen.blit(EMPico2 , [100 , 280])
        screen.blit(EMPico3 , [140 , 280])
        Instruction_text = pygame.font.Font(None , 32).render("Meduim fire rate doubles tower damage" , True , white)
        screen.blit(Instruction_text , [180 , 290])
    
        ##Laser
        Instruction_text = pygame.font.Font(None , 32).render("Laser:" , True , white)
        screen.blit(Instruction_text , [0 , 330])
        screen.blit(Laserico , [70 , 320])
        screen.blit(Laserico2 , [110 , 320])
        screen.blit(Laserico3 , [150 , 320])
        Instruction_text = pygame.font.Font(None , 32).render("Meduim fire rate meduim damage" , True , white)
        screen.blit(Instruction_text , [190 , 330])
        
        ##Rocket
        Instruction_text = pygame.font.Font(None , 32).render("Rocket:" , True , white)
        screen.blit(Instruction_text , [0 , 370])
        screen.blit(Rocketico , [80 , 360])
        screen.blit(Rocketico2 , [120 , 360])
        screen.blit(Rocketico3 , [160 , 360])
        Instruction_text = pygame.font.Font(None , 32).render("High damage low fire rate" , True , white)
        screen.blit(Instruction_text , [200 , 370])
        
        ##Super Tower
        Instruction_text = pygame.font.Font(None , 32).render("Super Tower:" , True , white)
        screen.blit(Instruction_text , [0 , 410])
        screen.blit(SuperTowerico , [140 , 400])
        Instruction_text = pygame.font.Font(None , 32).render("High Damage slow fire rate" , True , white)
        screen.blit(Instruction_text , [180 , 410])


        ##Back Button
        Back_Button = pygame.Surface([70 , 20])
        Back_Button.fill(gray)
        screen.blit(Back_Button , [550 , 440])
        Back_text = pygame.font.Font(None , 32).render("BACK!" , True , white)
        screen.blit(Back_text , [550 , 440])
        
        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                
                pt = pygame.mouse.get_pos()
                x , y = pt
                
                ##Back Button Clicked
                if x in range(550 , 621) and y in range(440 , 461):
                    screen.fill(black)
                    State = 0

            ##Escape is pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    screen.fill(black)
                    State = 0

                if event.key == K_m:
                    if not Music:
                        Music = True
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
                        Music = False
                    
            if event.type == QUIT:
                
                screen.fill(black)
                State = 0

    ##Tutorial
    elif State == 2:
        
        ##Background
        screen.blit(BG , (0,0))

        ##Title
        Title_text = pygame.font.Font(None , 100).render("TUTORIAL!" , True , white)
        screen.blit(Title_text , [100 , 0])

        ##Score Text
        Score_text = pygame.font.Font(None , 50).render("Score: 0" , True , white)
        screen.blit(Score_text , [0 , 70])

        ##Wave Text
        Wave_text = pygame.font.Font(None , 50).render("Wave: 1" , True , white)
        screen.blit(Wave_text , [250 , 70])

        if Stage == 0:
            
            ##Life Text
            Life_text = pygame.font.Font(None , 50).render("Life: 3" , True , white)
            screen.blit(Life_text , [500 , 70])

        elif Stage < 5:

            ##Life Text
            Life_text = pygame.font.Font(None , 50).render("Life: 2" , True , white)
            screen.blit(Life_text , [500 , 70])

        else:

            ##Life Text
            Life_text = pygame.font.Font(None , 50).render("Life: 1" , True , white)
            screen.blit(Life_text , [500 , 70])

        if not Stage == 8:
            ##Tag Text
            Tag_text = pygame.font.Font(None , 50).render("Tags : 0", True , white)
            screen.blit(Tag_text , [0 , 440])

        ##Next Button
        Next_Button = pygame.Surface([70 , 20])
        Next_Button.fill(gray)
        screen.blit(Next_Button , [550 , 440])
        Next_text = pygame.font.Font(None , 32).render("NEXT!" , True , white)
        screen.blit(Next_text , [550 , 440])

        ##Place the towers icon
        screen.blit(MachineGunico , (200 , 400))
        screen.blit(EMPico , (240 , 400))
        screen.blit(Laserico , (280 , 400))
        screen.blit(Rocketico , (320 , 400))
        screen.blit(SuperTowerico , (360 , 400))

        startingpositionx = 0
        startingpositiony = 280
        ##Draw the arena
        for i in range(0 , 16):
            for j in range(0 , 5):

                ##Place the floor
                screen.blit(floor , (i * 40 , j * 40 + 200))

                ##Place the entry gate
                if i == 0:
                    screen.blit(GateEntry , (i * 40 , j * 40 + 200))

                ##Place the exit gate
                if i == 15:
                    screen.blit(GateExit , (i * 40 , j * 40 + 200))

        ##Hide the towers
        if Stage < 2:   
            graysurface = pygame.Surface([200 , 40])
        else:
            graysurface = pygame.Surface([160 , 40])

        graysurface.fill(gray)
        graysurface.set_alpha(128)

        if Stage < 2:   
            screen.blit(graysurface , [200 , 400])
        else:
            screen.blit(graysurface , [240 , 400])
        

        ##Stage 0 of the tutorial
        if Stage == 0:

            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Enemies will enter from the left and leave from the right" , True , white)
            screen.blit(Instruction , [0 , 120])          

            if(len(tEnemy) == 0):
                tEnemy.append(EnemyTutorial(startingpositionx , startingpositiony))

            screen.blit(tEnemy[0].image , [tEnemy[0].x , tEnemy[0].y])
            tEnemy[0].update()

            if tEnemy[0].x >= resolution[0]:
                Stage += 1
                tEnemy = []

        ##Stage 1
        if Stage == 1:

            Instruction = pygame.font.Font(None , 32).render("Once an enemy reaches the end you lose one life" , True , white)
            screen.blit(Instruction , [0 , 120])

        ##Stage 2
        if Stage == 2:
            
            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Left click on the tower to place it" , True , white)
            screen.blit(Instruction , [0 , 120])

        if Stage == 3:
            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Move the mouse to position your tower" , True , white)
            screen.blit(Instruction , [0 , 120])

        if Stage == 4:

            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("The enemy will avoid the tower to reach the final destination" , True , white)
            screen.blit(Instruction , [0 , 120])
            tTower[0].coordinates(tRow  * 40 , 280)
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])
            if(len(tEnemy) == 0):
                tEnemy.append(EnemyTutorial(startingpositionx , startingpositiony))
            screen.blit(tEnemy[0].image , [tEnemy[0].x , tEnemy[0].y])
            tEnemy[0].avoid(tRow * 40 , 280)   
            tEnemy[0].update()
            tTower[0].lookat(tEnemy[0])
            if tEnemy[0].x >= resolution[0]:
                tEnemy =[]
                Stage += 1

        if Stage == 5:

            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("The enemy will avoid the tower to reach the final destination" , True , white)
            screen.blit(Instruction , [0 , 120])
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])

        if Stage == 6:

            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Left click on a tower to see it's range" , True , white)
            screen.blit(Instruction , [0 , 120])
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])

            if tTower[0].visible:
                tTower[0].showrange(screen)

        if Stage == 7:
            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Press H to hide the range" , True , white)
            screen.blit(Instruction , [0 , 120])
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])

            if visiblerange.visible:
                visiblerange.showrange(screen)

        if Stage == 8:

            ##Tag Text
            Tag_text = pygame.font.Font(None , 50).render("Tags : " + str(Tags) , True , white)
            screen.blit(Tag_text , [0 , 440])
            
            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Press U to upgrade the selected tower using your tags" , True , white)
            screen.blit(Instruction , [0 , 120])
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])

            if visiblerange.visible:
                visiblerange.showrange(screen)

        if Stage == 9:    
            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Upgraded towers has longer range and apply more damage" , True , white)
            screen.blit(Instruction , [0 , 120])
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])

            if visiblerange.visible:
                visiblerange.showrange(screen)

        if Stage == 10:
            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("The tower will shoot the enemy when in range" , True , white)
            screen.blit(Instruction , [0 , 120])
            if(len(tEnemy) == 0):
                tEnemy.append(EnemyTutorial(startingpositionx , startingpositiony))

            if tEnemy[0].health > 0:
                screen.blit(tEnemy[0].image , [tEnemy[0].x , tEnemy[0].y])

            else:
                Stage += 1

            tTower[0].shoot(tEnemy[0] , screen)
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])

            tEnemy[0].avoid(tRow * 40 , 280)   
            tEnemy[0].update()
            if tEnemy[0].x >= resolution[0]:
                tEnemy =[]
                Stage += 1

            if visiblerange.visible:
                visiblerange.showrange(screen)

        if Stage == 11:
            ##Instruction Text
            Instruction = pygame.font.Font(None , 32).render("Press R to delete selected tower" , True , white)
            screen.blit(Instruction , [0 , 120])
            screen.blit(tTower[0].image , [tTower[0].x , tTower[0].y])

            if visiblerange.visible:
                visiblerange.showrange(screen)

        if Stage == 12:
            ##Instruction Text
            Instruction = pygame.font.Font(None , 50).render("You have completed the tutorial!" , True , white)
            screen.blit(Instruction , [0 , 120])
            
        MouseMoving = False                    
        ##Event Handling
        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                
                pt = pygame.mouse.get_pos()
                x , y = pt

                if Stage == 1 or Stage == 5 or Stage == 9 or Stage == 12:
                    
                    ##Next Button Clicked
                    if x in range(550 , 621) and y in range(440 , 461):
                        screen.fill(black)
                        Stage += 1

                        if Stage == 13:
                            State = 0
                            tTower = []
                            tEnemy = []

                if Stage == 2:

                    ##Tower Clicked
                    if x in range(200 , 241) and y in range(400 , 441):
                        if len(tTower) == 0:
                            tTower.append(TowerTutorial())
                            Stage += 1
                            break

                if Stage == 6 or Stage > 7 and Stage < 12:

                    ##Tower Clicked
                    if x in range(tTower[0].x , tTower[0].x + 41) and y in range(tTower[0].y , tTower[0].y + 41):
                        tTower[0].showrange(screen)
                        visiblerange = tTower[0]

                        if Stage == 6:
                            Stage += 1

                ##Place Tower
                if Stage == 3:
                    
                    Stage += 1      

            if Stage == 3:
                if event.type == MOUSEMOTION:

                    MouseMoving = True

                    if not len(tTower) == 0:

                        tRow = int(pygame.mouse.get_pos()[0]/40)

                        if tRow <= 1 or tRow >= 13:

                            if tRow <= 1:
                                tRow = 2

                            if tRow>= 13:
                                tRow = 13
                        
                        screen.blit(tTower[0].image , (tRow  * 40 , 280))                        

            ##Escape is pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    screen.fill(black)
                    tTower = []
                    tEnemy = []
                    State = 0

                if event.key == K_m:
                    if not Music:
                        Music = True
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
                        Music = False

                if Stage > 6:

                    if event.key == K_h:
                        visiblerange.visible = False

                        if Stage == 7:
                            Stage += 1
                            Tags = 2

                if Stage == 8:
                    if event.key == K_u:

                        if visiblerange.visible:
                            if not visiblerange.level == 2:
                                visiblerange.upgrade()
                                Tags -= 1
                            else:
                                visiblerange.upgrade()
                                Tags -= 1
                                Stage += 1
                if Stage == 11:

                    if event.key == K_r:
                        if visiblerange.visible:

                            tTower = []
                            visiblerange = 0
                            Stage += 1
                
            if event.type == QUIT:
                screen.fill(black)
                tTower = []
                State = 0

        if Stage == 3:
            if not MouseMoving:
                if not len(tTower) == 0:
                    screen.blit(tTower[0].image , (tRow  * 40 , 280))

        

    ##Game Started
    elif State == 3:
        if WaveStarted:

            TimeCounter += 1

            if Waves > 30:
                EnemySpawn = 1

            elif Waves > 20:
                EnemySpawn = 2
                
            elif Waves > 10:
                EnemySpawn = 5

            elif Waves > 5:
                EnemySpawn = 10

            elif Waves > 3:
                EnemySpawn = 15

            ##Spawn Enemy
            if TimeCounter == EnemySpawn:
                if EnemySpawning:
                    if SpawnedEnemy < enemycount:

                        SpawnedEnemy += 1
                        
                        if (SpawnedEnemy % 5 == 0 and Waves >= 5) or (Waves > 10 and Waves % 5 == 0):

                            start = random.randint(0 , 9)
                            end = random.randint(0 , 9)
                            Path = astar(ArenaTiles , (0 , start) , (15 , end))
                            EnemyList.append(Tank(Path , TankImages))

                        elif SpawnedEnemy % 3 == 0 and Waves >= 3:
                            
                            start = random.randint(0 , 9)
                            end = random.randint(0 , 9)
                            Path = astar(HelicopterPath , (0 , start) , (15 , end))
                            EnemyList.append(Helicopter(Path , HelicopterImages))

                        else:

                            start = random.randint(0 , 9)
                            end = random.randint(0 , 9)
                            Path = astar(ArenaTiles , (0 , start) , (15 , end))
                            EnemyList.append(Buggy(Path , BuggyImages))

                    else:

                        EnemySpawning = False
                        FinishedSpawning = True
            
                    
        if FinishedSpawning:
            if WaveStarted:
                if len(EnemyList) == 0:
                    WaveStarted = False
                    Waves += 1

        ##When TimeCounter = 30 1 second has passed
        if TimeCounter == 30:
                Time += 1
                TimeCounter = 0

                if Time % 5 == 0:
                    if Tags < 20:
                        Tags += 1
                
        ##Background
        screen.blit(BG , (0,0))
        
        ##Draw the map
        for i in range(0 , 16):
            for j in range(0 , 10):

                ##Place the floor
                screen.blit(floor , (i * 40 , j * 40 + 40))

        ##Pop Enemies out of screen or died
        if WaveStarted:
            i = 0
            j = len(EnemyList)
            
            while i < j:

                if EnemyList[i].x >= 600:
                    EnemyList.pop(i)
                    Life -= 1
                    if Life == 0:
                        State = 4
                        ArenaTiles = []
                        SelectedTower = 0
                    j -= 1

                elif EnemyList[i].health <= 0:

                    Score += EnemyList[i].score
                    EnemyList.pop(i)
                    a = random.randint(0 , 100)
                    EnemyKilled += 1
                    if a < 25:
                        if Tags < 20:
                            Tags += 1
                    j -= 1

                else:
                    i += 1
                
        ##Update the enemies
        for i in range(0 , len(EnemyList)):
            EnemyList[i].Update()
            
        ##Draw the gate
        for i in range(0 , 10):
            
            screen.blit(GateEntry , [0 , i * 40 + 40])
            screen.blit(GateExit , [resolution[0] - 40 , i * 40 + 40])

        ##Draw the towers
        for i in range(0 , len(ArenaTiles)):
            for j in range(0 , len(ArenaTiles[0])):

                if not ArenaTiles[i][j] == 0:
                    if WaveStarted:
                        ArenaTiles[i][j].Update(EnemyList)
                    screen.blit(ArenaTiles[i][j].image, [i * 40 , j *40 + 40])

        ##Draw the enemies
        for i in range(0 , len(EnemyList)):
            screen.blit(EnemyList[i].image , [EnemyList[i].x , EnemyList[i].y])
                    

        ##Reset to middle of the screen
        if SelectedTower == 0:       
            tColumn = int(320 / 40)
            tRow = int(200 / 40)
        
        if WaveStarted:
            
            ##Wave Text
            Wave_text = pygame.font.Font(None , 50).render("Wave: " + str(Waves) , True , white)
            screen.blit(Wave_text , [250 , 0])

            ##Score Text
            Score_text = pygame.font.Font(None , 50).render("Score: " + str(Score) , True , white)
            screen.blit(Score_text , [0 , 0])

            ##Life Text
            Life_text = pygame.font.Font(None , 50).render("Life: " + str(Life) , True , white)
            screen.blit(Life_text , [500 , 0])

        else:

            ##Place your towers Text
            Wave_text = pygame.font.Font(None , 50).render("Place your towers" , True , white)
            screen.blit(Wave_text , [175 , 0])
            
        ##Tag Text
        Tag_text = pygame.font.Font(None , 50).render("Tags : " + str(Tags), True , white)
        screen.blit(Tag_text , [0 , 440])

        ##Time Text
        Time_text = pygame.font.Font(None , 50).render("Time : " + str(Time), True , white)
        screen.blit(Time_text , [450 , 440])

        ##Place the towers icon
        screen.blit(MachineGunico , (200 , 440))
        screen.blit(EMPico , (240 , 440))
        screen.blit(Laserico , (280 , 440))
        screen.blit(Rocketico , (320 , 440))
        screen.blit(SuperTowerico , (360 , 440))

        ##Hide the towers
        if Waves < 3:   
            graysurface = pygame.Surface([160 , 40])

        elif Waves < 5:
            graysurface = pygame.Surface([120 , 40])

        elif Waves < 10:
            graysurface = pygame.Surface([80 , 40])

        elif Waves < 20:
            graysurface = pygame.Surface([40 , 40])

        graysurface.fill(gray)
        graysurface.set_alpha(128)

        if Waves < 3:   
            screen.blit(graysurface , [240 , 440])

        elif Waves < 5:
            screen.blit(graysurface , [280 , 440])

        elif Waves < 10:
            screen.blit(graysurface , [320 , 440])

        elif Waves < 20:
            screen.blit(graysurface , [360 , 440])


        MouseMoving = False

        ##Event Handling
        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:

                pt = pygame.mouse.get_pos()
                x , y = pt

                ##Placing Towers
                if not WaveStarted:

                    if SelectedTower == 0:

                        
                        ##Machine Gun Selected
                        if x in range(200 , 241) and y in range(440 , 481):
                            SelectedTower = T_MachineGun(screen , MG)
                            SelectedTower.SetCoordinates(tColumn * 40 , tRow * 40)
                            PlacingTower = True
                            
                        if Waves >= 3:

                            ##EMP Selected
                            if x in range(240 , 281) and y in range(440 , 481):
                                SelectedTower = T_EMP(screen , EMP)
                                SelectedTower.SetCoordinates(tColumn * 40 , tRow * 40)
                                PlacingTower = True

                        if Waves >= 5:
                        ##Laser Selected
                            if x in range(280 , 321) and y in range(440 , 481):
                                SelectedTower = T_Laser(screen , Laser)
                                SelectedTower.SetCoordinates(tColumn * 40 , tRow * 40)
                                PlacingTower = True

                        if Waves >= 10:
                            ##Rocket Selected
                            if x in range(320 , 361) and y in range(440 , 481):
                                SelectedTower = T_Rocket(screen , Rocket)
                                SelectedTower.SetCoordinates(tColumn * 40 , tRow * 40)
                                PlacingTower = True

                            if Waves >= 20:
                                ##Super Tower Selected
                                if x in range(360 , 401) and y in range(440 , 481):
                                    SelectedTower = T_SuperTower(screen , SuperTower)
                                    SelectedTower.SetCoordinates(tColumn * 40 , tRow * 40)
                                    PlacingTower = True

                        ##Check if an already placed tower was selected
                        if y in range(40 , 440):
                            
                            if y > 400:
                                y = 400
                                
                            tColumn = int(x/ 40)
                            tRow = int(y/40) - 1

                            if not ArenaTiles[tColumn][tRow] == 0:
                                ArenaTiles[tColumn][tRow].ShowRange()
                                SelectedTower = (tColumn , tRow)
                                PlacingTower = False
                            

                    else:

                        if PlacingTower:

                            if y < 40:
                                y = 40
                            if y > 400:
                                y = 400

                            tColumn = int(x/ 40)
                            tRow = int(y/40) - 1

                            if tColumn < 2:
                                tColumn = 2

                            if tColumn > 13:
                                tColumn = 13

                            ##Prevent placing two towers at the same place
                            if ArenaTiles[tColumn][tRow] == 0:
                                ArenaTiles[tColumn][tRow] = 1
                                if astar(ArenaTiles , (0,0) , (15 , 0)):
                                    ArenaTiles[tColumn][tRow] = SelectedTower
                                    ArenaTiles[tColumn][tRow].SetCoordinates(tColumn * 40 , tRow * 40 + 40)
                                    PlacingTower = False
                                    SelectedTower = 0
                                else:
                                    ArenaTiles[tColumn][tRow] = 0

                ##Wave Started
                else:

                    ##Check if an already placed tower was selected
                    if y in range(40 , 440):
                        
                        if y > 400:
                            y = 400
                            
                        tColumn = int(x/ 40)
                        tRow = int(y/40) - 1

                        if not ArenaTiles[tColumn][tRow] == 0:
                            ArenaTiles[tColumn][tRow].ShowRange()
                            SelectedTower = (tColumn , tRow)

                    

            if not WaveStarted:       
                if not SelectedTower == 0:
                    if PlacingTower:
                        
                        if event.type == MOUSEMOTION:
                            MouseMoving = True

                            pt = pygame.mouse.get_pos()
                            x , y = pt

                            if y < 40:
                                y = 40
                            if y > 400:
                                y = 400
                            tColumn = int(x/ 40)
                            tRow = int(y/40)

                            if tColumn < 2:
                                tColumn = 2

                            if tColumn > 13:
                                tColumn = 13

                            SelectedTower.SetCoordinates(tColumn * 40 , tRow * 40)
                            screen.blit(SelectedTower.image , [SelectedTower.x , SelectedTower.y])
                            SelectedTower.ShowRange()

            ##Escape is pressed
            if event.type == KEYDOWN:

                if WaveStarted:
                    if event.key == K_PERIOD:
                        if fps == 30:
                            fps = 45
                        elif fps == 45:
                            fps = 60
                    if event.key == K_COMMA:
                        if fps == 45:
                            fps = 30
                        elif fps == 60 :
                            fps = 45

                if not WaveStarted:
                    if event.key == K_p:
                        WaveStarted = True
                        EnemySpawning = True
                        FinishedSpawning = False
                        enemycount = random.randint(Waves * 10 , Waves * 30)
                        SpawnedEnemy = 0

                if not SelectedTower == 0:

                    if PlacingTower:

                        if event.key == K_r:

                            SelectedTower = 0
                            

                    if not PlacingTower:

                        if not WaveStarted:
                            ##Remove an already placed tower
                            if event.key == K_r:
                                ArenaTiles[SelectedTower[0]][SelectedTower[1]] = 0
                                SelectedTower = 0

                        ##Deselect the tower
                        if event.key == K_h:
                            SelectedTower = 0

                        if event.key == K_u:

                            if not Tags == 0:
                                if ArenaTiles[SelectedTower[0]][SelectedTower[1]].level < 3:
                                    ArenaTiles[SelectedTower[0]][SelectedTower[1]].Upgrade()
                                    Tags -= 1
                                    
                if event.key == K_ESCAPE:
                    screen.fill(black)
                    ArenaTiles = []
                    SelectedTower = 0
                    State = 4

                if event.key == K_m:
                    if not Music:
                        Music = True
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
                        Music = False
            
            if event.type == QUIT:
                screen.fill(black)
                ArenaTiles = []
                SelectedTower = 0
                State = 0

        ##Places the tower in the position the mouse was last
        if not SelectedTower == 0:

            if PlacingTower:
                    
                if not MouseMoving:

                    screen.blit(SelectedTower.image , [tColumn * 40 , tRow * 40])
                    SelectedTower.ShowRange()
            else:

                ArenaTiles[SelectedTower[0]][SelectedTower[1]].ShowRange()

    ##Game Over Screen
    if State == 4:

        ##Background
        screen.blit(BG , (0,0))

        ##Stats
        Stats_text = pygame.font.Font(None , 50).render("Statistics:" , True , white)
        screen.blit(Stats_text , [250 , 0])

        ##Wave Text
        Wave_text = pygame.font.Font(None , 32).render("You Survied: " + str(Waves) + " Waves" , True , white)
        screen.blit(Wave_text , [0 , 50])

        ##Enemy Killed
        Enemy_text = pygame.font.Font(None , 32).render("You Killed: " + str(EnemyKilled) + " Enemies" , True , white)
        screen.blit(Enemy_text , [0 , 100])

        ##Score Killed
        Score_text = pygame.font.Font(None , 32).render("You Scored: " + str(Score) + " Points" , True , white)
        screen.blit(Score_text , [0 , 150])

        ##Time Survived
        Time_text = pygame.font.Font(None , 32).render("Time Played: " + str(Time) + " Seconds" , True , white)
        screen.blit(Time_text , [0 , 200])

        ##Next Button
        Next_Button = pygame.Surface([70 , 20])
        Next_Button.fill(gray)
        screen.blit(Next_Button , [550 , 440])
        Next_text = pygame.font.Font(None , 32).render("NEXT!" , True , white)
        screen.blit(Next_text , [550 , 440])
        
        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                
                pt = pygame.mouse.get_pos()
                x , y = pt
                
                ##Next Button Clicked
                if x in range(550 , 621) and y in range(440 , 461):
                    screen.fill(black)
                    State = 0

            ##Escape is pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    screen.fill(black)
                    State = 0

                if event.key == K_m:
                        if not Music:
                            Music = True
                            pygame.mixer.music.play(-1)
                        else:
                            pygame.mixer.music.stop()
                            Music = False
                    
            if event.type == QUIT:
                
                screen.fill(black)
                State = 0

    pygame.display.update()


pygame.quit()
quit()

        
