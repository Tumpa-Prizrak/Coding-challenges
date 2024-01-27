from sand_simulation import config


class Cell:
    def __init__(self, x: int, y: int, is_filled: bool = False) -> None:
        self.x = x
        self.y = y
        self.is_filled = is_filled

    def __abs__(self):
        return self.x * config.RECT_SIZE, self.y * config.RECT_SIZE, \
                config.RECT_SIZE, config.RECT_SIZE, 

    def get_color(self):
        return config.ACTIVE_COLOR if self.is_filled else config.INACTIVE_COLOR
