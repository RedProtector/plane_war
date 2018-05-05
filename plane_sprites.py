import random
import pygame

SCREEN_SIZE = (480,700)
HERO_POSITION = (200,550)
ENEMY_EVENT = pygame.USEREVENT
BULLET_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite)  :
    """"飞机大战精灵"""
    def __init__(self,image_path,speed = 1) :
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.speed = speed
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed

class BackGround(GameSprite):
    def __init__(self,alt = True):
        super().__init__('./images/background.png')
        self.speed = 1
        if alt == False:
            self.rect.y = self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.bottom = 0

class Hero(GameSprite):
    def __init__(self):
        super().__init__('./images/me1.png')
        self.rect.centerx = SCREEN_SIZE[0]/2
        self.rect.y = SCREEN_SIZE[1] - 130
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_RIGHT]:
            self.rect.x += 3
        elif key_event[pygame.K_LEFT]:
            self.rect.x -= 3
        if self.rect.x >= 378:
            self.rect.x = 378
        if self.rect.x <= 0:
            self.rect.x = 0

    def fire(self):
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - 20*i
            self.bullet_group.add(bullet)

class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./images/enemy1.png')
        self.speed = random.randint(2, 5)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_SIZE[0] - self.rect.width)
    def update(self):
        super().update()
        if self.rect.y  >= SCREEN_SIZE[1]:
            self.kill()

class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/bullet1.png')
        self.bullet_boom = pygame.sprite.Group()

    def update(self):
        self.rect.y -= self.speed*1.5
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        bullet_boom = Bullet_Boom()
        self.bullet_boom.add(bullet_boom)

class Bullet_Boom(GameSprite):
    def __init__(self):
        pass
