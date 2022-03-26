# modules
import os
import beta_Jogo_15 as a
from settings import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

white = (255, 255, 255)
black = (0, 0, 0)
red = (150, 0, 0)
blue = (0, 0, 150)
bright_red = (255, 0, 0)
bright_blue = (0, 111, 255)
gray = (245, 245, 245)
light_blue = (0, 196, 255)

WIN_WIDTH = 800
WIN_HEIGHT = 600
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

clock = pygame.time.Clock()


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(MSG, SIZE=150, color=black, ):
    global screen
    # # screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

    text = pygame.font.SysFont("freesansbold.ttf", SIZE)  # FONT E TAMANHO PERSONALIZADO
    TextSurf, TextRect = text_objects(MSG, text, color)  # A TORNAR MENSAGEM EM OBJETO
    TextRect.center = ((WIN_WIDTH / 2), (WIN_HEIGHT / 2))  # MEIO DO ECRA

    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    # TEMPO DE ESPERA
    time.sleep(5)

    a.game()


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««

def text_to_button(text, x, y, w, h, color, size=20):
    global screen

    text2 = pygame.font.SysFont("freesansbold.ttf", 20)  # FONT E TAMANHO
    textSurf, TextRect = text_objects(text, text2, color)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))  # CENTER FINDER
    screen.blit(textSurf, TextRect)


def button(msg, x, y, w, h, ic, ac, action=None, color=black):
    global screen

    mouse = pygame.mouse.get_pos()  # MOUSE POSITION
    click = pygame.mouse.get_pressed()  # WHAT WAS PRESSED ON MOUSE

    #  X + WITDH > XRATO > X & Y + HEIGHT > YRATO > Y
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))  # SCREEN + ACTIVE COLOR + X, Y , WIDHT e HEIGHT
        # CLICK(ESQUERDA, MEIO, DIREITA) == CLICK[0,1,2] = (0,0,0) == WHEN CLICKED = 1 (1,0,0) SE ESQUERDA CLICADA
        # != NOT EQUAL
        if click[0] == 1 and action != None:
            if action == "play":
                a.level = 1
                a.game()

            if action == "quit":
                pygame.event.post(pygame.event.Event(QUIT))
        else:
            pass
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))  # SCREEN + INACTIVE COLOR + X, Y , WIDHT e HEIGHT

    text_to_button(msg, x, y, w, h, color)


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
def menu_intro():
    global screen
    intro = True
    bg = pygame.image.load(resource_path("img/menu_inicial.png"))
    bg.convert()
    screen.blit(bg, (0, 0))

    while intro:

        pygame.display.update()

        clock.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()

            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

        # TEXTO, X, Y, WIDHT, HEIGHT, INACTIVE COLOR, ACTIVE COLOR, ACTION
        button("Play!", 250, 450, 300, 50, light_blue, bright_blue, action="play")
        pygame.display.update()
        button("Quit!", 350, 510, 100, 50, red, bright_red, action="quit")
