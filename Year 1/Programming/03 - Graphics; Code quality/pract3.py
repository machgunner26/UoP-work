from graphix import Window, Point, Circle, Line, Rectangle, Polygon, Text, Entry
import math

def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)

def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)

def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()

# Problem 1
def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    arms = Line(Point(150, 200), Point(250, 200))
    arms.draw(win)
    leg_one = Line(Point(150, 300), Point(200, 240))
    leg_one.draw(win)
    leg_two = Line(Point(200, 240), Point(250, 300))
    leg_two.draw(win)

# Problem 2
def draw_circle():
    radius = int(input("Enter the radius of the circle: "))
    win = Window()
    circle = Circle(Point(200, 200), radius)
    circle.draw(win)

# Problem 3
def draw_archery_target():
    win = Window("Archery Target")
    blue_circle = Circle(Point(200, 200), 150)
    blue_circle.draw(win)
    blue_circle.fill_colour = "blue"
    red_circle = Circle(Point(200, 200), 100)
    red_circle.draw(win)
    red_circle.fill_colour = "red"
    yellow_circle = Circle(Point(200, 200), 50)
    yellow_circle.draw(win)
    yellow_circle.fill_colour = "yellow"

# Problem 4
def draw_rectangle():
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the hegiht of the rectangle: "))
    top_left_x = 200 - (width // 2)
    top_left_y = 200 - (height // 2)
    bottom_right_x = 200 + (width // 2)
    bottom_right_y = 200 + (height // 2)
    win = Window()
    rectangle = Rectangle(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))
    rectangle.draw(win)

# Problem 5
def blue_circle():
    win = Window()
    centre = win.get_mouse()
    circle = Circle(centre, 100)
    circle.draw(win)
    circle.fill_colour = "blue"

# Problem 6
def ten_lines():
    win = Window()
    message = Text(Point(200, 50), "")
    for i in range(10):
        message.text = "click on the first point"
        message.draw(win)
        p1 = win.get_mouse()
        message.text = "click on the second point"
        p2 = win.get_mouse()
        line = Line(p1, p2)
        line.draw(win)
        message.undraw()
    message.text = "click anywhere to quit"
    message.draw(win)
    win.get_mouse()
    win.close()

# Problem 7
def ten_strings():
    win = Window("Window", 500, 500)
    message = Text(Point(250, 50), "Enter your text below & click on the window where you want it")
    message.draw(win)
    input_box = Entry(Point(250, 100), 30)
    input_box.draw(win)
    for i in range(10):
        position = win.get_mouse()
        text = Text(position, input_box.text)
        text.draw(win)
    message.text = "Click anywhere to exit"
    win.get_mouse()
    win.close()

# Problem 8
def ten_coloured_rectangles():
    win = Window()
    instructions = Text(Point(200, 25), "Enter the colour of the rectangle")
    instructions.draw(win)
    message = Text(Point(200, 50), "")
    message.draw(win)
    input_box = Entry(Point(200, 100), 10)
    input_box.text = "blue"
    input_box.draw(win)

    for i in range(10):
        message.text = "click on first point"
        top_left = win.get_mouse()
        message.text = "click on second point"
        bottom_right = win.get_mouse()
        rectangle = Rectangle(top_left, bottom_right)
        rectangle.draw(win)
        rectangle.fill_colour = input_box.text

    message.text = "Click anywhere to quit"
    win.get_mouse()
    win.close()

# Problem 9
def five_click_stick_figure():
    win = Window()
    point_1 = win.get_mouse()
    point_2 = win.get_mouse()
    x_difference = point_2.x - point_1.x
    y_difference = point_2.y - point_1.y
    radius = round(math.sqrt(x_difference**2 + y_difference**2))
    head = Circle(point_1, radius)
    head.draw(win)
    point_3 = win.get_mouse()
    body = Line(Point(point_1.x, point_1.y + radius), Point(point_1.x, point_3.y))
    body.draw(win)
    point_4 = win.get_mouse()
    arms = Line(Point(point_4.x, point_4.y), Point(2 * point_1.x - point_4.x, point_4.y))
    arms.draw(win)
    point_5 = win.get_mouse()
    leg_1 = Line(point_5, Point(point_1.x, point_3.y))
    leg_1.draw(win)
    leg_2 = Line(Point(2 * point_1.x - point_5.x, point_5.y), Point(point_1.x, point_3.y))
    leg_2.draw(win)
    win.get_mouse()
    win.close()