import math
from graphix import Window, Circle, Point, Text

def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divide_and_product(a, b):
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result


def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product_result, divide_result = divide_and_product(num1, num2)
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")


def calc_future_value(amount, years):
    interest_rate = 0.065
    for year in range(years):
        amount = amount * (1 + interest_rate)
    return amount


def future_value():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# For exercises 1 and 2
def area_of_circle(radius):
    return math.pi * radius ** 2

# Problem 1
def circumference_of_circle(radius):
    return 2 * math.pi * radius

# Problem 2
def circle_info():
    radius = float(input("Enter the radius: "))
    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)
    print(f"The area is {area:.3f} and the circumference is {circumference:.3f}")


# For exercise 3
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)

def draw_brown_eye_in_centre():
    window = Window()
    centre = Point(200, 200)
    draw_circle(window, centre, 120, "white")
    draw_circle(window, centre, 60, "brown")
    draw_circle(window, centre, 30, "black")
    window.get_mouse()
    window.close()

# Problem 4
def draw_block_of_stars(width, height):
    for i in range(height):
        print("*" * width)
        
def draw_letter_e():
    draw_block_of_stars(8, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(5, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(8, 2)

# For exercise 5
def draw_brown_eye(win, centre, radius):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, int(radius / 2), "brown")
    draw_circle(win, centre, int(radius / 3), "black")
    
def draw_pair_of_brown_eyes():
    win = Window("Brown Eyes", 400, 400)
    draw_brown_eye(win, Point(125, 200), 75)
    draw_brown_eye(win, Point(275, 200), 75)
    win.get_mouse()
    win.close()
    

# Problem 6
def distance_between_points(p1, p2):
    x_difference = p2.x - p1.x
    y_difference = p2.y - p1.y
    distance = math.sqrt(x_difference ** 2 + y_difference ** 2)
    return distance

# Problem 7
def distance_calculator():
    win = Window()
    message = Text(Point(200, 200), "Click two points")
    message.draw(win)
    point1 = win.get_mouse()
    point2 = win.get_mouse()
    distance = distance_between_points(point1, point2)
    message.text = str(distance)
    win.get_mouse()
    win.close()
    
# Problem 8
def draw_blocks(spaces1, asterisks1, spaces2, asterisks2, height):
    for i in range(height):
        message = ""
        message += " " * spaces1
        message += "*" * asterisks1
        message += " " * spaces2
        message += "*" * asterisks2
        print(message)
        
def draw_letter_a():
    draw_blocks(1, 8, 1, 0, 2)
    draw_blocks(0, 2, 6, 2, 2)
    draw_blocks(0, 10, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 3)
    
# Problem 9
def draw_four_pairs_of_brown_eyes():
    win = Window()
    for i in range(4):
        centre = win.get_mouse()
        outer_point = win.get_mouse()
        radius = distance_between_points(centre, outer_point)
        draw_brown_eye(win, centre, int(radius))
        draw_brown_eye(win, Point(int(centre.x + radius * 2.5), centre.y), int(radius))
    win.get_mouse()
    win.close()
    
# Problem 10
def display_text_with_spaces(text, size, position, window):
    string = 
    print(string)
    message = Text(position, string.upper())
    message.size = size
    message.draw(window)