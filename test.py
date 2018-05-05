import random
import pygame

ENEMY_EVENT = pygame.USEREVENT

# 游戏初始化
pygame.init()

# 创建游戏窗口对象
screen = pygame.display.set_mode((480,700))

# 绘制图像并显示
# 1，导入图片数据
bg_img = pygame.image.load('./images/background.png')
enemy_img = pygame.image.load('./images/enemy1.png')
hero_img = pygame.image.load('./images/me1.png')
bullet_img = pygame.image.load('./images/bullet1.png')

# 2，利用屏幕对象在指定位置绘制图像
screen.blit(bg_img,(0,0))
screen.blit(enemy_img,(0,0))
screen.blit(hero_img,(200,550))
screen.blit(bullet_img,(251,539))

# 3，更新屏幕
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

print("game is coming...")

pygame.time.set_timer(ENEMY_EVENT,5000)
i = random.randint(0,5) * 80
enemy_rect = pygame.Rect(i,0,69,99)

hero_rect = pygame.Rect(200,550,102,126)

bullet_rect = pygame.Rect(251,539,5,11)

while True :
    # 设置刷新帧率
    clock.tick(60)

    screen.blit(bg_img, (0, 0))

    #  退出游戏事件监听
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        elif event.type == ENEMY_EVENT :
            i = random.randint(0, 5) * 80
            enemy_rect = pygame.Rect(i, 0, 69, 99)

    #  控制战机移动
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_RIGHT] :
        hero_rect.x += 3
    elif key_event[pygame.K_LEFT] :
        hero_rect.x -=3
    if hero_rect.x >= 378 :
        hero_rect.x = 378
    if hero_rect.x <= 0 :
        hero_rect.x = 0
    screen.blit(hero_img,hero_rect)

    # 发射子弹
    bullet_rect.x = hero_rect.x + hero_rect.width * 0.5
    bullet_rect.y -= 3
    screen.blit(bullet_img,bullet_rect)

    # 让敌机飞行
    enemy_rect.y += 3
    if enemy_rect.y >= 700:
        enemy_rect.y = -99
    screen.blit(enemy_img, enemy_rect)

    # 让战机循环飞行
    # hero_rect.y -= 3
    # if hero_rect.y <= -126 :
    #     hero_rect.y = 700
    # screen.blit(hero_img, hero_rect)

    pygame.display.update()

pygame.quit()