import pygame
from sand_simulation.classes.matrix import Matrix
from sand_simulation import config
from sand_simulation import physics
pygame.init()


def main():
    screen = pygame.display.set_mode(
        [
            config.WIDTH_CELLS * config.RECT_SIZE, 
            config.HEIGHT_CELLS * config.RECT_SIZE
        ]
    )
    clock = pygame.time.Clock()

    grid = Matrix(config.WIDTH_CELLS, config.HEIGHT_CELLS)
    grid.fill(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    grid.get(event.pos[0] // config.RECT_SIZE, event.pos[1] // config.RECT_SIZE).is_filled = True
                elif event.button == 3:
                    grid.get(event.pos[0] // config.RECT_SIZE, event.pos[1] // config.RECT_SIZE).is_filled = False

        physics.update_physics(grid)
        screen.fill((0, 0, 0))
        for cell in grid.get_draw_list():
            pygame.draw.rect(screen, cell[1], cell[0])

        pygame.display.flip()
        clock.tick(24)
        # print("Frame!")

if __name__ == "__main__":
    main()
    pygame.quit()
