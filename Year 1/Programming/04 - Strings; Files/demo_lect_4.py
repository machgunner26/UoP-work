from graphix import Window, Rectangle, Circle, Point, Text
# import time

def move_car():
    win = Window("",700,400)
    
    sentence = "this is the best sentence"
    words = sentence.split()
    revealed_sentence = ""
    
    x = 100
    y = 150
    car_body_width = 200
    car_body_height = 50
    
    tl = Point(x, y)
    br = Point(x + car_body_width, y + car_body_height)
    
    car_body = Rectangle(tl, br)
    car_body.fill_colour = "blue"
    car_body.draw(win)
    
    x_circle = x + 50
    y_circle = y + car_body_height
    
    centre_point_1 = Point(x_circle, y_circle)
    
    radius = 30
    
    wheel1 = Circle(centre_point_1, radius)
    wheel1.fill_colour = "black"
    wheel1.draw(win)
    
    x_circle += 100
    
    centre_point_2 = Point(x_circle, y_circle)
    
    wheel2 = Circle(centre_point_2, radius)
    wheel2.fill_colour = "Black"
    wheel2.draw(win)
    
    text_box = Text(Point(350, 50), "")
    text_box.draw(win)
    
    step = 5
    
    for word in words:
        # time.sleep(0.25)
        win.get_mouse()
        
        car_body.move(step, 0)
        wheel1.move(step, 0)
        wheel2.move(step, 0)
        
        revealed_sentence += word + " "
        text_box.text = revealed_sentence
    
    win.get_mouse()
    win.close()
    
move_car()