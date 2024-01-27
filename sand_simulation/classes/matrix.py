from sand_simulation.classes.cell import Cell


class Matrix:
    __data: tuple[tuple[Cell, ...], ...]
    height: int
    width: int

    def __init__(self, width: int, height: int) -> None:
        self.__data = tuple(tuple(Cell(w, h) for w in range(width)) for h in range(height))
        self.height = height
        self.width = width

    def get(self, x: int, y: int):
        return self.__data[y][x]

    def fill(self, is_filled: bool):
        for row in self.__data:
            for cell in row:
                cell.is_filled = is_filled

    def get_draw_list(self):
        for row in self.__data:
            for cell in row:
                yield abs(cell), cell.get_color()
    
    def set_activity(self, x: int, y: int, is_filled: bool):
        self.__data[y][x].is_filled = is_filled
