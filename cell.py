from graphics import Line, Point


class Cell:
    def __init__(
        self,
        top_left,
        bottom_right,
        window,
        left=True,
        right=True,
        top=True,
        bottom=True,
    ):
        # What walls does the cell have?
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        # Set points for line makeup
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = window
        # Define walls
        self._left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))

    def draw(self):
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
