import pygame
pygame.init()

# 画面設定
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("フォントテスト")

# フォント設定
font = pygame.font.Font("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 32)

# 描画
text_surf = font.render("答え: 2", True, (255,255,0))
screen.fill((0,0,0))
screen.blit(text_surf, (50,50))
pygame.display.flip()

# 終了待ち
input("Enterで終了")
pygame.quit()
