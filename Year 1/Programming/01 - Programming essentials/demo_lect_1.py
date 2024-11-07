# Problem 1: Simple Output
def problem_1():
    print("""Welcome to The Media Hub!
We have been serving entertainment enthusiasts since 1995.""")

# Problem 2: Multiple Outputs
def problem_2():
    print("""Welcome to The Media Hub!
We have been serving entertainment enthusiasts since 1995.
Location: 123 Entertainment Avenue, Mediaville
Speciality: Rare and vintage films, music, and games""")

# Problem 3: Numerical Input and Calculation
def problem_3():
    print("""Welcome to The Media Hub!
We have been serving entertainment enthusiasts since 1995.""")
    age = int(input("Please enter your age: "))
    birthYear = 2024 - age
    print(birthYear)
    if (birthYear > 1995):
        print("You were born in " + str(birthYear) + ", " + str(birthYear - 1995) + " years after our opening!")
    elif (birthYear < 1995):
        print("You were born in " + str(birthYear) + ", " + str(1995 - birthYear) + " years before our opening!")
    else:
        print("You were born in 1995, the year we opened!")

# Problem 4: Two Inputs and Calculation
def problem_4():
    print("Welcome to The Media Hub!")
    max = int(input("Enter a number: "))
    count = 1
    while (count <= max):
        print(count)
        count = count + 1

# Problem 5: Multiple Inputs
def problem_5():
    print("Welcome to The Media Hub!")
    max = int(input("Enter a number: "))
    count = 1
    while (count <= max):
        print(count)
        count = count + 1

# Problem 6: Fixed Loop
def problem_6():
    print("Welcome to The Media Hub!")
    count = 0
    while (count < 5):
        print("I love entertainment!")
        count = count + 1
        
# Problem 7: User-Defined Loop
def problem_7():
    print("Welcome to The Media Hub!")
    max = int(input("Enter a number: "))
    count = 1
    while (count <= max):
        print(count)
        count = count + 1
        
# Problem 8: Loop with Incrementing Output
def problem_8():
    print("Welcome to The Media Hub!")
    max = int(input("Enter a number: "))
    count = 1
    while (count <= max):
        print(count)
        count = count + 1
        
# Problem 9: Loop with Calculations
def problem_10():
    print("Welcome to The Media Hub!")
    max_rating = int(input("Enter the maximum rating for the scale: "))
    print("Rating scale up to", max_rating, ":")
    count = 1
    while count <= max_rating:
        print(count, "

# Problem 10: Complex Loop with Initial Inputs
def problem_11():
    x = 1