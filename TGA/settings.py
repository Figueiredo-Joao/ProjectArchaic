import os
import pygame, sys
from pygame import *
import time
#modules
import map1
import enemy
##import button

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


WIN_WIDTH = 800
WIN_HEIGHT = 600
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

HS_FILE = resource_path("highscore.txt")

FPS = 60

TITLE = "Jogo_Beta!"

#CORES
white = (255,255,255)
black = (0,0,0)
red = (150,0,0)
blue = (0,0,150)
bright_red = (255,0,0)
bright_blue = (0,0,255)
gray = (245,245,245)


