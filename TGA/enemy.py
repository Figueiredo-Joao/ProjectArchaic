import os
import IMAGENS as i
from settings import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

red = (150, 0, 0)

pygame.font.init()
entities = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

##enemyskilled = 0
SCORE = 0

##««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
##animar os inimigos

class enemy_1(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = -1        
        self.yvel = 0
        
        self.onGround = False
        self.destroyed = False
        self.counter = 0
        self.rightside = True
        self.enemykilled = 0

        self.faceright = False
        
        self.image = i.enemywalk1
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)
        
    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3

            if self.yvel > 100: self.yvel = 100


        self.rect.left += self.xvel

        self.collide(self.xvel, 0, platforms, entities)

        self.rect.top += self.yvel

        self.onGround = False

        self.collide(0, self.yvel, platforms, entities)

        self.animate()
        

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -abs(xvel)
                    self.faceright = False

                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)
                    self.faceright = True

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    
        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.xvel = 0
                    
    def animate(self):
        if not self.destroyed:
            self.walkloop()
            self.counter = self.counter + 1
        else: self.destroyloop()

    def walkloop(self):
        if self.counter == 1:
            self.updatecharacter(i.enemykill)
        elif self.counter == 15:
            self.updatecharacter(i.enemywalk1)
        elif self.counter == 30:
            self.updatecharacter(i.enemywalk2)
        elif self.counter == 45:
            self.updatecharacter(i.enemywalk3)
        elif self.counter == 60:
            self.updatecharacter(i.enemywalk4)
        elif self.counter == 75:
            self.updatecharacter(i.enemywalk2)
        elif self.counter == 90:
            self.updatecharacter(i.enemywalk1)
            self.counter = 0
        
        
    def destroyloop(self):
        
        if self.counter == 0:
            self.updatecharacter(i.enemykill)
        elif self.counter == 5:
            self.updatecharacter(i.enemykill2)
        elif self.counter == 10:
            global SCORE
            SCORE += 1
            self.kill()
            
        self.counter = self.counter + 1
        

    def updatecharacter(self, ansurf):
        if self.faceright: ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

#<==================================================================

class enemy_2(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0

        self.onGround = False
        self.destroyed = False
        self.counter = 0
        self.enemykilled = 0

        self.faceright = False

        self.image = i.batwalk1
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self, platforms, entities):
        self.onGround = False

        self.animate()

        self.collide(entities)



    def collide(self, entities):
        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.xvel = 0

    def animate(self):
        if not self.destroyed:
            self.walkloop()
            self.counter = self.counter + 1
        else:
            self.destroyloop()

    def walkloop(self):
        if self.counter == 1:
            self.updatecharacter(i.batwalk1)
        elif self.counter == 15:
            self.updatecharacter(i.batwalk2)
        elif self.counter == 30:
            self.updatecharacter(i.batwalk3)
        elif self.counter == 45:
            self.updatecharacter(i.batwalk4)
        elif self.counter == 60:
            self.updatecharacter(i.batwalk3)
        elif self.counter == 75:
            self.updatecharacter(i.batwalk2)
        elif self.counter == 90:
            self.counter = 0

    def destroyloop(self):

        if self.counter == 0:
            self.updatecharacter(i.batwalk1)
        elif self.counter == 5:
            self.updatecharacter(i.batkill)
        elif self.counter == 10:
            global SCORE
            SCORE += 1
            self.kill()

        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        if self.faceright: ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf


scorefont = pygame.font.SysFont("freesansbold.ttf", 30) #FONT E TAMANHO PERSONALIZADO
score = scorefont.render("Score: " + str(SCORE), True, red)
TextRect = score.get_rect()

HS_FILE = resource_path("highscore.txt")

class load_data():
    global SCORE
##    dir = path.dirname(__file__)


    with open(HS_FILE, 'wb') as f:
        try:
            highscore = f.read()
##            highscore.append(int(f.read(HS_FILE)))
            highscore = int(highscore)
        except:
            highscore = 0








