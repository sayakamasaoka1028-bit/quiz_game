import pygame

pygame.init()

# ウィンドウ作成
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("テストウィンドウ")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # 黒で塗りつぶし
    pygame.display.flip()

pygame.quit()
