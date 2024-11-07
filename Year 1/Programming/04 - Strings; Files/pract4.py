from graphix import Window, Point, Circle, Line, Rectangle, Polygon, Text, Entry
import os

def student_info():
    course = input("What's your course? ")
    student_id = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + student_id[2:])


def personal_details():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def read_quote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))
    # Change directory to the folder containing quotation.txt
    os.chdir("text_files")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    input_file = open("quotation.txt", "r")

    # You can use `read()` to read the whole file into a single string
    content = input_file.read()
    print(content)


def write_quote():
    os.chdir("text_files")
    output_file = open("my_quotation.txt", "w")

    # You can use `write()` to write a single string
    print("I love Python!", file=output_file)
    print("(Matthew Poole)", file=output_file)

    # Or write both lines in one go separated by a newline character ('\n')
    # content = "I love Python!\n(Matthew Poole)"
    # output_file.write(content)


# Solutions below:

# Problem 1
def personal_greeting():
    name = input("Enter your name: ")
    print(f"Hello {name}, nice to see you!")
    
# Problem 2
def formal_name():
    name = input("Enter your name: ")
    family_name = input("Enter your family name: ")
    print(f"{name[0].upper()}. {family_name}")
    
# Problem 3
def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print(f"{kilos:.2f} kilos is equal to {ounces:.2f} ounces")
    
# Problem 4
def generate_email():
    forename = input("Enter your forename: ")
    surname = input("Enter your surname: ")
    year = input("Enter the year starting at the university: ")
    print(f"{surname[0:4].lower()}.{forename[0].lower()}.{year}@myport.ac.uk")
    
# Problem 5
def grade_test():
    grades = "FFFFCCBBAAA"
    mark = int(input("Enter the number of marks: "))
    student_grade = grades[mark]
    print(student_grade)
    
# Problem 6
def graphic_letters():
    word = input("Enter a word: ")
    win = Window()
    for i in word:
        position = win.get_mouse()
        letter = Text(position, i)
        letter.draw(win)
        letter.size = 30
    win.get_mouse()
    win.close()
    
# Problem 7
def sing_a_song():
    word = input("Enter a word: ")
    lines = int(input("Enter the number of lines: "))
    words_repeated = int(input("Enter the nubmer of times you want the word repeated: "))
    
    line = ""
    
    for i in range(words_repeated):
        line += " " + word
        
    for i in range(lines):
        print(line)
        
# Problem 8
def exchange_table():
    print("Euros\tPounds")
    for i in range(20):
        euros = i + 1
        pounds = euros / 1.17
        print(f"{euros:2}\t{pounds:5.2f}")

# Problem 9
def make_initialism():
    phrase = input("Enter a phrase: ")
    words = phrase.split(" ")
    letters = ""
    for word in words:
        letters += word[0]
    print(letters.upper())
    
# Problem 10
def file_in_caps():
    file = input("Enter the name of a file: ")
    os.chdir("text_files")
    text_file = open(file, "r")
    content = text_file.read()
    print(content.upper())

# Problem 11
def total_spending():
    os.chdir("text_files")
    text_file = open("spending.txt", "r")
    content = text_file.read()
    days = content.split("\n")
    total = 0
    for day in days:
        total += float(day)
    print(f"£{total}")
    
# Problem 12
def name_to_number():
    name = input("Enter your name: ")
    name = name.lower()
    total = 0
    for letter in name:
        total += ord(letter) - 96
    print(total)
        
# Problem 13
def rainfall_chart():
    os.chdir("text_files")
    text_file = open("rainfall.txt", "r")
    content = text_file.read()
    cities = content.split("\n")
    for city in cities:
        city_split = city.split(" ")
        rainfall = int(city_split[1])
        asterisk = "*" * rainfall
        print(f"{city_split[0]} {asterisk}")
        
def rainfall_graphics():
    os.chdir("text_files")
    text_file = open("rainfall.txt", "r")
    content = text_file.read()
    cities = content.split("\n")
    win = Window("Rainfall", 800, 400)
    pos_y = 30
    for city in cities:
        city_split = city.split(" ")
        rainfall = int(city_split[1])
        
        name = Text(Point(100, pos_y), city_split[0])
        name.draw(win)
        
        rectangle = Rectangle(Point(200, pos_y - 10), Point(200 + (10 * rainfall), pos_y + 10))
        rectangle.draw(win)
        
        pos_y += 30
    win.get_mouse()
    win.close()
    
# Problem 14
def rainfall_in_inches():
    os.chdir("text_files")
    text_file = open("rainfall.txt", "r")
    content = text_file.read()
    cities = content.split("\n")
    output_file = open("rainfallInches.txt", "w")
    for city in cities:
        city_split = city.split(" ")
        city_split[1] = round(int(city_split[1]) / 25.4, 2)
        city = f"{city_split[0]} {city_split[1]}"
        print(city, file=output_file)
    output_file.close()

# Problem 15
def wc():
    os.chdir("text_files")
    file = input("Enter the name of the file: ")
    text_file = open(file, "r")
    content = text_file.read()
    
    lines = content.split("\n")
    line_count = 0
    for line in lines:
        line_count += 1
    
    words = content.split(" ")
    word_count = 0
    for word in words:
        word_count += 1
        
    character_count = 0
    for character in content:
        character_count += 1
    
    print(f"{line_count}\t{word_count + 2}\t{character_count}")