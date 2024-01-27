from sand_simulation.classes.matrix import Matrix


def update_physics(grid: Matrix):
    for h in range(grid.height - 1, 1, -1):
        for w in range(grid.width - 1, 0, -1):
            if not grid.get(w, h).is_filled and grid.get(w, h - 1).is_filled:
                grid.get(w, h).is_filled = True
                grid.get(w, h - 1).is_filled = False
