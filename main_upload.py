# Pygame-CE + PyScript
# Kullanıcının seçtiği resmi JS ile /uploads altına yazıyoruz.
# Python tarafında periyodik kontrol edip resmi pygame.image.load ile yüklüyoruz.

import pygame, asyncio, os

W, H = 640, 360
BG = (20, 24, 36)

pygame.init()
screen = pygame.display.set_mode((W, H))
clock  = pygame.time.Clock()

# Kullanıcının yükleyebileceği olası yollar
CANDIDATES = ["/uploads/selected.png", "/uploads/selected.jpg"]

sprite = None
rect = pygame.Rect(W//2-40, H//2-40, 80, 80)  # sprite yoksa placeholder
vx = 3

async def try_load_sprite():
    """EMFS içine yazılmış bir görsel varsa bir kere yükle."""
    global sprite, rect
    if sprite is not None:
        return
    for path in CANDIDATES:
        if os.path.exists(path):
            try:
                tmp = pygame.image.load(path)
                # Alfa varsa koru, yoksa convert()
                sprite = tmp.convert_alpha() if tmp.get_alpha() else tmp.convert()
                rect = sprite.get_rect(center=(W//2, H//2))
                return
            except Exception as e:
                # Hatalı ya da desteklenmeyen resim ise atla
                print("Yükleme hatası:", e)

async def main():
    global sprite, rect, vx
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        # Dosya geldiyse bir kez yüklemeyi dene
        await try_load_sprite()

        # Basit hareket
        rect.x += vx
        if rect.right >= W or rect.left <= 0:
            vx *= -1

        # Çizim
        screen.fill(BG)
        if sprite is None:
            # Placeholder kutu (dosya seçilene kadar)
            pygame.draw.rect(screen, (220, 70, 70), rect, width=0)
            # İnce çerçeve
            pygame.draw.rect(screen, (250, 220, 220), rect, width=2)
        else:
            screen.blit(sprite, rect)

        pygame.display.flip()
        await asyncio.sleep(1/60)

    pygame.quit()

asyncio.run(main())
