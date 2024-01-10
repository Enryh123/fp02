import pygame
pygame.init()

width = 288
height = 512

# 3. 创建时钟


# 7. 创建自定义事件



window = pygame.display.set_mode((width, height))
pygame.display.set_caption('flappy bird')

bg_image = pygame.image.load('images/background-day.png')

# 5. 使用bird列表存储鸟的图片，并删除bird_image

bird_image = pygame.image.load('images/bluebird-midflap.png')
bird_rect = bird_image.get_rect()
bird_rect.center = (width / 2, height / 2)

# 1. 地板图片与矩形区域



while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()

        # 8. 判断自定义事件并实现鸟动画



    window.blit(bg_image, (0, 0))


    # 6. 使用列表访问鸟的图片并绘制
    
    window.blit(bird_image, bird_rect)


    # 2. 绘制地板并移动



    pygame.display.update()

    # 4. 设置帧率
