# modules
import os
import IMAGENS
import enemy as en
from button import *
from enemy import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pygame.font.init()

# VARIAVEIS
level: int = 1
nextlevel = False
map1.mymap = []
platforms = []
entities = pygame.sprite.Group()
dead = True

collide = False

HS_FILE = resource_path("highscore.txt")

pygame.display.set_caption('The Great Adventure')

def game():
    global screen, SCORE, scorefont, score, rectanglefont, dead, level
    dead = False
    bg = pygame.image.load(resource_path("img/background.png"))
    bg.convert()

    enemy.load_data()

    up = down = left = right = running = False

    enemygroup = pygame.sprite.Group()

    player = Player(32*2, 32*2)

    constructionMaps(enemygroup)

    while 1:
        global nextlevel, last_right, last_left



        total_level_width = len(map1.mymap[1]) * 32  ##Mudar valor tamanho x da camera
        total_level_height = len(map1.mymap) * 32  ##Mudar valor tamanho y da camera
        camera = Camera(complex_camera, total_level_width, total_level_height)
        entities.add(player)

        nextlevel = False

        while 1:
            clock.tick(60)

            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    exit()

                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit()
                    exit()

                if e.type == KEYDOWN and e.key == K_UP or e.type == KEYDOWN and e.key == K_w or e.type == KEYDOWN and e.key == K_SPACE:
                    up = True
                if e.type == KEYDOWN and e.key == K_DOWN or e.type == KEYDOWN and e.key == K_s:
                    down = True
                if e.type == KEYDOWN and e.key == K_LEFT or e.type == KEYDOWN and e.key == K_a:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT or e.type == KEYDOWN and e.key == K_d:
                    right = True
                if e.type == KEYDOWN and e.key == K_RSHIFT:
                    running = True

                if e.type == KEYUP and e.key == K_UP or e.type == KEYUP and e.key == K_w or e.type == KEYUP and e.key == K_SPACE:
                    up = False
                if e.type == KEYUP and e.key == K_DOWN or e.type == KEYUP and e.key == K_s:
                    down = False
                if e.type == KEYUP and e.key == K_RIGHT or e.type == KEYUP and e.key == K_d:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT or e.type == KEYUP and e.key == K_a:
                    left = False
                if e.type == KEYUP and e.key == K_RSHIFT:
                    running = False

            # background

            screen.blit(bg, (0, 0))  ## coloca bg no 0,0

            # SCORES E HIGHSCORES

            SCORE = enemy.SCORE  # VARIAVEL DE OUTRO MODULE
            SCORE = SCORE * 100
            scorefont = enemy.scorefont  # VARIAVEL DE OUTRO MODULE
            score = scorefont.render("Score: " + str(SCORE), True, red)
            rect = en.TextRect  # VARIAVEL DE OUTRO MODULE
            rect.center = (80, 10)
            screen.blit(score, rect)

            HIGHSCORE = en.load_data.highscore
            highscorefont = pygame.font.SysFont("freesansbold.ttf", 30)
            highscore = highscorefont.render("Highscore: " + str(HIGHSCORE), True, red)
            rect = en.TextRect  # VARIAVEL DE OUTRO MODULE
            rect.center = (WIN_WIDTH - 150, 10)
            screen.blit(highscore, rect)

            if SCORE > (HIGHSCORE):
                HIGHSCORE = SCORE

                ##                dir = path.dirname(__file__)
                with open(HS_FILE, 'w') as f:
                    f.write(str(HIGHSCORE))
            else:
                pass

            camera.update(player)

            # update player, desanha o resto
            player.update(up, down, left, right, running, platforms, enemygroup)

            for e in entities:
                screen.blit(e.image, camera.apply(e))

            for e in enemygroup:
                screen.blit(e.image, camera.apply(e))
                e.update(platforms, entities)

            pygame.display.update()


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««

def main():
    pygame.init()  # inicia o pygame
    pygame.font.init()  # inicia a escrita de entidades
    menu_intro()  # Menu inicial
    game()  # Corre o mapa1 do jogo


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««


def constructionMaps(enemygroup):
    global plataforms, entities, collide, level, dead, nextlevel
    x = y = 0

    map1.maps(level, enemygroup)

    # constroi mapa
    for row in map1.mymap:
        for col in row:

            if col != " " and col != "X" and col != "t" and col != "Z":
                if dead == False:
                    if col == "A":
                        i.qual_plataforma(x, y, 1)
                    elif col == "B":
                        i.qual_plataforma(x, y, 2)
                    elif col == "C":
                        i.qual_plataforma(x, y, 3)
                    elif col == "D":
                        i.qual_plataforma(x, y, 4)
                    elif col == "E":
                        i.qual_plataforma(x, y, 5)
                    elif col == "F":
                        i.qual_plataforma(x, y, 6)
                    elif col == "G":
                        i.qual_plataforma(x, y, 7)
                    elif col == "H":
                        i.qual_plataforma(x, y, 8)
                    elif col == "I":
                        i.qual_plataforma(x, y, 9)
                    elif col == "J":
                        i.qual_plataforma(x, y, 10)
                    elif col == "K":
                        i.qual_plataforma(x, y, 11)
                    elif col == "L":
                        i.qual_plataforma(x, y, 12)
                    elif col == "M":
                        i.qual_plataforma(x, y, 13)
                    elif col == "N":
                        i.qual_plataforma(x, y, 14)
                    elif col == "O":
                        i.qual_plataforma(x, y, 15)
                    elif col == "P":
                        i.qual_plataforma(x, y, 16)
                    elif col == "Q":
                        i.qual_plataforma(x, y, 17)
                    elif col == "R":
                        i.qual_plataforma(x, y, 18)
                    elif col == "S":
                        i.qual_plataforma(x, y, 19)
                    elif col == "T":
                        i.qual_plataforma(x, y, 20)
                    elif col == "U":
                        i.qual_plataforma(x, y, 21)

            if col == "X":
                if dead == False:
                    k = Killer(x, y)
                    platforms.append(k)
                    entities.add(k)
                    collide = True

            if col == "t":
                if dead == False:
                    t = Transporter(x, y)
                    platforms.append(t)
                    entities.add(t)
                    collide = False

            if col == "Z":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)

            x += 32
        y += 32
        x = 0


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

    l = min(0, l)  # QUANDO CHEGA AO LIMITE ESQUERDO PARA!
    l = max(-(camera.width - WIN_WIDTH), l)  # QUANDO CHEGA AO LIMITE DIREITO PARA!
    t = max(-(camera.height - WIN_HEIGHT), t)  # QUANDO CHEGA AO CHAO PARA!
    t = min(0, t)  # QUANDO BATER NO TETO PARA!
    return Rect(l, t, w, h)


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
class Player(Entity):
    global last_right, last_left, dead, level

    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0

        self.faceright = True
        self.onGround = False
        self.airborne = True

        self.counter = 0
        self.counter2 = 0
        self.counter3 = 0

        self.destroy = False

        self.image = i.stand
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, running, platforms, enemygroup):
        if up:
            # saltar quando esta no chão
            if self.onGround: self.yvel -= 10

        if down:
            pass

        if running:
            self.xvel = 25

        if left:
            self.xvel = -8
            self.faceright = False

        if right:
            self.xvel = 8
            self.faceright = True

        if not (right or left):
            self.xvel = 0

        if not self.onGround:
            # mover no ar
            self.yvel += 0.5
            if down:
                self.yvel += 0.5

            # velocidade de queda
            if self.yvel > 8: self.yvel = 8

        if self.destroy == True:
            global dead
            pygame.event.post(pygame.event.Event(QUIT))
            dead = True
            self.destroy = False

        if self.yvel < 0 or self.yvel > 1.2: self.airborne = True
        # mover horizontal
        self.rect.left += self.xvel
        # colizoes x
        self.collide(self.xvel, 0, platforms, enemygroup)
        # saltar
        self.rect.top += self.yvel
        # não chao
        self.onGround = False
        # colizao y
        self.collide(0, self.yvel, platforms, enemygroup)

        self.animate()

    ##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
    def collide(self, xvel, yvel, platforms, enemygroup):
        global collide
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    global level
                    self.deading(platforms, enemygroup)
                    level += 1
                    message_display("VICTORY!", 150, color=red)

                if isinstance(p, Transporter):
                    if pygame.sprite.collide_rect(self, p):
                        platforms.remove(p)
                        entities.remove(p)
                        enemy.SCORE += 5

                if isinstance(p, Killer):
                    if pygame.sprite.collide_rect(self, p):
                        dif = p.rect.bottom - self.rect.top
                        if dif <= 8:
                            pass
                        else:
                            self.kys(platforms, enemygroup)

                if collide == True:  # Se bater Player == STOP
                    if xvel > 0:
                        self.rect.right = p.rect.left
                    if xvel < 0:
                        self.rect.left = p.rect.right
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.airborne = False
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                else:  # Senao == CONTINUE
                    pass

        # morrer se tocar em inimigo
        for e in enemygroup:
            if pygame.sprite.collide_rect(self, e):

                dif = self.rect.bottom - e.rect.top
                if dif <= 8:
                    self.yvel = - 8

                else:
                    self.counter3 = 5
                    self.kys(platforms, enemygroup)

    def deading(self, platforms, enemygroup):
        self.kill()
        self.remove()

        platforms.clear()
        enemygroup.empty()
        entities.empty()



##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
##animar a personagem e demais

    def animate(self):
        if self.xvel > 0 or self.xvel < 0:
            self.walkloop()
            self.counter2 = 0

            if self.airborne:
                self.jumploop()
                self.counter = 0

        elif self.xvel == 0 and self.yvel == 0:
            self.idle()
            self.counter = 0

        else:
            if self.airborne:
                self.jumploop()
                self.counter = 0

    def jumploop(self):

        if self.yvel < 5 and self.yvel > -5:
            self.updatecharacter(i.saltar_2)
        elif self.yvel < 6:
            self.updatecharacter(i.saltar_1)
        elif self.yvel > -6:
            self.updatecharacter(i.saltar_3)

    def idle(self):
        if self.counter2 == 0:
            self.updatecharacter(i.stand)
        elif self.counter2 == 15:
            self.updatecharacter(i.stand_2)
        elif self.counter2 == 30:
            self.updatecharacter(i.stand)
            self.counter2 = 0
        self.counter2 = self.counter2 + 1

    def kys(self, platforms, enemygroup):

        if self.counter3 == 0:
            self.updatecharacter(i.death_1)

        elif self.counter3 == 1:
            self.updatecharacter(i.death_2)

        elif self.counter3 == 2:
            self.updatecharacter(i.death_3)

        elif self.counter3 == 3:
            self.updatecharacter(i.death_4)

        elif self.counter3 == 4:
            self.updatecharacter(i.death_5)

        elif self.counter3 == 5:

            self.deading(platforms, enemygroup)
            enemy.SCORE = 0

            # PODE-SE ESPECIFICAR OS CAMPOS COM ORDENS DIFERENTES
            # OU DEIXAR PREDEFENIDOS NA FUNÇÃO, NAO SENDO PRECISO ADICIONAR O CAMPO
            message_display("YOU DIED", 150, color=red)

        self.counter3 = self.counter3 + 1

    def walkloop(self):
        if self.counter == 5:
            self.updatecharacter(i.walk_1)
        elif self.counter == 10:
            self.updatecharacter(i.walk_2)
        elif self.counter == 15:
            self.updatecharacter(i.walk_3)

        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        if not self.faceright: ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf


##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««

class Platform(Entity):
    def __init__(self, x, y, img):
        Entity.__init__(self)
        self.image = img
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass


class Killer(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(resource_path("img/Killers.png"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass


class Transporter(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.counter = 0

        self.image = i.points1
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass


class ExitBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(resource_path("img/platform.png"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)


if __name__ == "__main__":
    main()
