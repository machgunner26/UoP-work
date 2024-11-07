import math

# Group Worksheet A
def average():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    average = (num1 + num2) / 2
    print("The average of the two numbers is", average)

# Problem 1
def speed_calculator():
    distance = float(input("Enter the distance travelled in km: "))
    time = float(input("Enter the time of the journey in hours: "))
    speed = distance / time
    print("The average speed in km/h is", speed)
    
# Problem 2
def circumference_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * radius * math.pi
    print("The circumference of the circle is", circumference)
    
# Problem 3
def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = radius**2 * math.pi
    print("The area of the circle is", area)
    
# Problem 4
def cost_of_pizza():
    diameter = float(input("Enter the diameter of the pizza in cm: "))
    area = (math.pi * diameter**2) / 4
    cost = area * 0.035
    print("The cost of the pizza is", cost)
    
# Problem 5
def slope_of_line():
    x_1 = int(input("Enter the x value of the first coordinate: "))
    y_1 = int(input("Enter the y value of the first coordinate: "))
    x_2 = int(input("Enter the x value of the second coordinate: "))
    y_2 = int(input("Enter the y value of the second coordinate: "))
    x_change = x_2 - x_1
    y_change = y_2 - y_1
    slope = y_change / x_change
    print("The slope of the line is", slope)
    
# Problem 6
def distance_between_points():
    x_1 = int(input("Enter the x value of the first coordinate: "))
    y_1 = int(input("Enter the y value of the first coordinate: "))
    x_2 = int(input("Enter the x value of the second coordinate: "))
    y_2 = int(input("Enter the y value of the second coordinate: "))
    x_change = x_2 - x_1
    y_change = y_2 - y_1
    distance = math.sqrt(y_change**2 + x_change**2)
    print("The distance ebtween the two points is", distance)

# Problem 7
def travel_statistics():
    speed = int(input("Enter the average speed of the journey in km/h: "))
    duration = float(input("Enter the duration of the journey in hours: "))
    distance = speed * duration
    fuel_used = distance * 5
    print("The total distance travelled is", distance)
    print("The fuel used is", fuel_used)
    
# Problem 8
def sum_of_squares():
    total = 0
    integer = int(input("Enter an integer: "))
    for i in range(integer):
        total = total + (i + 1)**2
    print(total)

# Problem 9
def average_of_numbers():
    number_input = int(input("Enter the number of numbers you are going to input: "))
    total = 0
    for i in range(number_input):
        number = int(input("Enter a number: "))
        total = total + number
    average = total / number_input
    print("The average of the nubmers you have entered is", average)
    
# Problem 10
def fibonacci():
    n = int(input("Enter a number: "))
    second_last_value = 0
    last_value = 0
    current_value = 0
    for i in range(n):
        print(current_value)
        current_value = second_last_value + last_value

# Problem 11
def select_coins():
    amount = int(input("Enter an amount of money in pence: "))
    two_pound = amount // 200
    amount = amount % 200
    one_pound = amount // 100
    amount = amount % 100
    fifty_pence = amount // 50
    amount = amount % 50
    twenty_pence = amount // 20
    amount = amount % 20
    ten_pence = amount // 10
    amount = amount % 10
    five_pence = amount // 5
    amount = amount % 5
    two_pence = amount // 2
    amount = amount % 2
    one_pence = amount // 1
    print(f"{two_pound} × £2, {one_pound} × £1, {fifty_pence} × 50p, {twenty_pence} × 20p, {ten_pence} × 10p, {five_pence} × 5p, {two_pence} × 2p, {one_pence} × 1p")