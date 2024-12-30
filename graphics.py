from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    # Takes a Canvas (from tkinter) and fill colour, fill colour being e.g. "black", "red"
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_one.x,
            self.point_one.y,
            self.point_two.x,
            self.point_two.y,
            fill=fill_color,
            width=2,
        )


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
            self._win.draw_line(self._left_wall, "black")
        # Draw right wall
        if self.has_right_wall:
            self._win.draw_line(self._right_wall, "black")
        # Draw top wall
        if self.has_top_wall:
            self._win.draw_line(self._top_wall, "black")
        # Draw bottom wall
        if self.has_bottom_wall:
            self._win.draw_line(self._bottom_wall, "black")
