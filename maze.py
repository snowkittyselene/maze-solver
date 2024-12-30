from cell import Cell
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        if seed:
            random.seed(seed)

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        # Create the cells
        self._cells = []
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)

        # Draw the cells
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Get cell size
        cell_x1 = self._x1 + (i * self._cell_size_x)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = self._y1 + (j * self._cell_size_y)
        cell_y2 = cell_y1 + self._cell_size_y

        # Draw cell
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0:  # Left
                if not self._cells[i - 1][j].visited:
                    to_visit.append("left")
            if j > 0:  # Up
                if not self._cells[i][j - 1].visited:
                    to_visit.append("up")
            if i < self._num_cols - 1:  # Right
                if not self._cells[i + 1][j].visited:
                    to_visit.append("right")
            if j < self._num_rows - 1:  # Down
                if not self._cells[i][j + 1].visited:
                    to_visit.append("down")

            # If we can't go anywhere, leave
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            # Move randomly and break the wall, then move to that cell
            dir = random.randrange(len(to_visit))
            if to_visit[dir] == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)
            if to_visit[dir] == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j - 1].has_right_wall = False
                self._break_walls_r(i - 1, j)
            if to_visit[dir] == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                self._break_walls_r(i, j + 1)
            if to_visit[dir] == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
