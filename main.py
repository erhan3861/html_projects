# Pygame-CE + PyScript: Görseli PyScript 'files' ile FS'e kopyalayıp klasik load
import pygame, asyncio

W, H = 640, 360
BG = (20, 24, 36)

pygame.init()
screen = pygame.display.set_mode((W, H))
clock  = pygame.time.Clock()

# Dosya, PyScript 'files' ile /home/pyodide içine kopyalandı → normal load yeterli
sprite = pygame.image.load("robot_arm.png").convert_alpha()
sprite = pygame.transform.scale(sprite, (64, 64))
rect = sprite.get_rect(center=(W//2, H//2))
vx = 3

async def main():
    global rect, vx
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        rect.x += vx
        if rect.right >= W or rect.left <= 0:
            vx *= -1

        if pygame.mouse.get_pressed()[0]:
            rect.center = pygame.mouse.get_pos()
            
        screen.fill(BG)
        screen.blit(sprite, rect)
        pygame.display.flip()

        # Tarayıcıyı kilitlememek için:
        await asyncio.sleep(1/60)

    pygame.quit()

asyncio.run(main())
