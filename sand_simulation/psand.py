from typing import Self


class Grit:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def update(self, xs: list[int], ys: list[int]):
        if self.y - 1 not in ys:
            self.y -= 1
