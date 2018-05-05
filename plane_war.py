import pygame
from plane_sprites import *

class PlaneGame(object):

    # 游戏初始化
    def __init__(self):
        pygame.init()
        # 创建屏幕对象
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        # 创建游戏时钟
        self.clock = pygame.time.Clock()

        # 创建定时器
        self.timer1 = pygame.time.set_timer(ENEMY_EVENT, 1000)
        self.timer2 = pygame.time.set_timer(BULLET_EVENT, 500)

        # 创建精灵和精灵组
        self.__create_sprites()

    def start_game(self):
        while True:
            self.clock.tick(60)

            self.bg_sprites_group.update()
            self.bg_sprites_group.draw(self.screen)

            self.__event_handler()
            self.enemy_group.update()
            self.enemy_group.draw(self.screen)

            self.hero_group.update()
            self.hero_group.draw(self.screen)

            self.hero.bullet_group.update()
            self.hero.bullet_group.draw(self.screen)

            self.__check_collide()

            pygame.display.update()


    def __create_sprites(self):
        # 设置背景图片，并使其滚动
        self.bg1 = BackGround()
        self.bg2 = BackGround(False)
        self.hero = Hero()

        self.bg_sprites_group = pygame.sprite.Group(self.bg1,self.bg2)
        self.bg_sprites_group.update()
        self.bg_sprites_group.draw(self.screen)

        self.enemy_group = pygame.sprite.Group()

        self.hero_group = pygame.sprite.Group(self.hero)

        self.hero.bullet_group = pygame.sprite.Group()

        pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == BULLET_EVENT:
                self.hero.fire()

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        collide = pygame.sprite.groupcollide(self.hero_group,self.enemy_group,True,True)
        if collide.__len__() > 0 :
            pygame.quit()
            exit()

if __name__ == '__main__':
    plan_game = PlaneGame()





