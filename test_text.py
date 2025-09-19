import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("数字テスト")
font = pygame.font.Font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)

text_surface = font.render("1+1=?", True, (255,255,255))
screen.blit(text_surface, (50,50))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
