from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        # What walls does the cell have?
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # Set points for when drawing
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        # Set up points
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2
        # Define walls
        self._left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self.center = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        # Draw left wall
        if self.has_left_wall:
            self._win.draw_line(self._left_wall)
        # Draw right wall
        if self.has_right_wall:
            self._win.draw_line(self._right_wall)
        # Draw top wall
        if self.has_top_wall:
            self._win.draw_line(self._top_wall)
        # Draw bottom wall
        if self.has_bottom_wall:
            self._win.draw_line(self._bottom_wall)

    # Draws a line between the center of two cells
    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        center_line = Line(self.center, to_cell.center)
        self._win.draw_line(center_line, color)
