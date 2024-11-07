from graphix import Window, Text, Point

def hello_graphix():
    input_text = input("enter a word: ")
    
    win = Window("my first window", 400, 700)
    
    point = Point(200, 350)
    
    text = "hello " + input_text
    
    message = Text(point, text)
    message.draw(win)
    
    for i in range(10):
        win.get_mouse()
        message.move(0, -20)
    
    win.get_mouse()
    win.close()
    

hello_graphix()