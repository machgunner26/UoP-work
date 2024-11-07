from graphix import Window, Rectangle, Point
import random
import time

WIDTH = 100   # Width and height of each rectangle
HEIGHT = 100  # Height of each rectangle (same as width in this case for squares)
RADIUS = 50   # Radius for circles
WIN_SIZE = 500  # Window size

def draw_rectangle(window, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.fill_colour = colour
    rectangle.draw(window)
    
def main():
    win = Window("", WIN_SIZE, WIN_SIZE)
    colour = "blue"
    colours = ["blue", "green", "red", "yellow", "purple", "orange", "black", "pink"]
    for x in range(5):
        time.sleep(0.1)
        for i in range(5):
            time.sleep(0.1)
            p1 = Point(0 + i * 100, 0 + x * 100)
            p2 = Point(WIDTH + i * 100, HEIGHT + x * 100)
            draw_rectangle(win, p1, p2, colours[random.randint(0,7)])
    win.get_mouse()
    win.close()
    
main()