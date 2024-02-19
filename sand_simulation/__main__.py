import pygame
from sand_simulation.psand import Grit

pygame.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
running = True

pieces: list[Grit] = []
pieces.append(Grit(0, 0))


def process_list(pieces: list):
    x: list[int] = []
    y: list[int] = []

    for piece in pieces:
        x.append(piece.x)
        x.append(piece.y)
    
    return x,y



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    xs, ys = process_list(pieces)

    for grit in pieces:
        grit.update(xs, ys)
        pygame.draw.rect(screen, (255, 255, 255), (grit.x, grit.y, 1, 1))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()