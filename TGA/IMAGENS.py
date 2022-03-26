import os
import beta_Jogo_15
from settings import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
# frames de personagens
character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_idle.png"))
stand = character

character = Surface((32, 27), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_idle_2.png"))
stand_2 = character

character = Surface((32, 29), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_jump_1.png"))
saltar_1 = character

character = Surface((32, 30), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_jump_2.png"))
saltar_2 = character

character = Surface((32, 29), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_jump_3.png"))
saltar_3 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_right_1.png"))
walk_1 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_right_2.png"))
walk_2 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_right_3.png"))
walk_3 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_death_1.png"))
death_1 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_death_2.png"))
death_2 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_death_3.png"))
death_3 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_death_4.png"))
death_4 = character

character = Surface((32, 25), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/char_death_5.png"))
death_5 = character

##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
##FRAMES dos inimigos

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Frog_Move1.png"))
enemywalk1 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Frog_Move2.png"))
enemywalk2 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Frog_Move3.png"))
enemywalk3 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Frog_Move4.png"))
enemywalk4 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Frog_Idle.png"))
enemykill = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Frog_Hurt.png"))
enemykill2 = character

##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
##FRAMES dos enemy_2
character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Bat.png"))
batwalk1 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Bat_Move1.png"))
batwalk2 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Bat_Move2.png"))
batwalk3 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Bat_Move3.png"))
batwalk4 = character

character = Surface((32, 26), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/Bat_Hurt.png"))
batkill = character

##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
##FRAMES dos pointblocks
character = Surface((24, 32), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/points.png"))
points1 = character

character = Surface((24, 32), pygame.SRCALPHA)
character = pygame.image.load(resource_path("img/points_2.png"))
points2 = character


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
##Texturas de PLATAFORMAS

def qual_plataforma(x, y, pos):
    if pos == 1:
        plataforma = pygame.image.load(resource_path("img/Grass_End_Left.png"))
    elif pos == 2:
        plataforma = pygame.image.load(resource_path("img/Grass_Middle.png"))
    elif pos == 3:
        plataforma = pygame.image.load(resource_path("img/Grass_End_Right.png"))
    elif pos == 4:
        plataforma = pygame.image.load(resource_path("img/Dirt_Middle_End_Left.png"))
    elif pos == 5:
        plataforma = pygame.image.load(resource_path("img/Dirt_Middle_Middle.png"))
    elif pos == 6:
        plataforma = pygame.image.load(resource_path("img/Dirt_Middle_End_Right.png"))
    elif pos == 7:
        plataforma = pygame.image.load(resource_path("img/Dirt_End_Hill_Right.png"))
    elif pos == 8:
        plataforma = pygame.image.load(resource_path("img/Dirt_End_Sky_Bottom.png"))
    elif pos == 9:
        plataforma = pygame.image.load(resource_path("img/Dirt_End_Hill_Left.png"))
    elif pos == 10:
        plataforma = pygame.image.load(resource_path("img/Grass_Platform_End_Left.png"))
    elif pos == 11:
        plataforma = pygame.image.load(resource_path("img/Grass_Platform_Middle.png"))
    elif pos == 12:
        plataforma = pygame.image.load(resource_path("img/Grass_Platform_End_Right.png"))
    elif pos == 13:
        plataforma = pygame.image.load(resource_path("img/Grass_End_Hill_Right.png"))
    elif pos == 14:
        plataforma = pygame.image.load(resource_path("img/Dirt_End_Sky_Right.png"))
    elif pos == 15:
        plataforma = pygame.image.load(resource_path("img/Grass_End_Hill_Left.png"))
    elif pos == 16:
        plataforma = pygame.image.load(resource_path("img/Dirt_End_Sky_Left.png"))
    elif pos == 17:
        plataforma = pygame.image.load(resource_path("img/Dirt_Middle_IDK.png"))
    elif pos == 18:
        plataforma = pygame.image.load(resource_path("img/Grass_End_Top.png"))
    elif pos == 19:
        plataforma = pygame.image.load(resource_path("img/Dirt_Both_Ends.png"))
    elif pos == 20:
        plataforma = pygame.image.load(resource_path("img/Dirt_End_Other_Side.png"))
    elif pos == 21:
        plataforma = pygame.image.load(resource_path("img/Dirt_End_Other_Side_idk.png"))

    platform = plataforma
    p = beta_Jogo_15.Platform(x, y, platform)

    beta_Jogo_15.platforms.append(p)
    beta_Jogo_15.entities.add(p)
    beta_Jogo_15.collide = True
