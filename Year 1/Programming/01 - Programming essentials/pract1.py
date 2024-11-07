def say_hello():
    print("Hello World")

def say_bye():
    print("Goodbye Mars")

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print("The weight in ounces is", ounces)

def count():
    for number in range(10):
        print("Number is now:", number)

def euros_to_pounds():
    euros = float(input("Enter a value in euros: "))
    pounds = euros * 0.87
    print("The value in pounds is", pounds)


# Problem 1
def say_name():
    print("James")

# Problem 2
def say_name_2():
    print("hello")
    print("world")

# Problem 3
def dollars_to_pounds():
    dollars = float(input("Enter an amount in dollars: "))
    pounds = round(dollars / 1.35, 2)
    print("That is £", pounds)

# Problem 4
def sum_and_difference():
    number_1 = float(input("Enter a number: "))
    number_2 = float(input("Enter another number: "))
    sum = number_1 + number_2
    difference = number_1 - number_2
    print("The sum of the two numbers is:", sum)
    print("The difference of the two numbers is:", difference)

# Problem 5
def change_counter():
    one_pence = int(input("How many 1 pence coins do you have? "))
    two_pence = int(input("How many 2 pence coins do you have? "))
    five_pence = int(input("How many 5 pence coins do you have? "))
    total = (1 * one_pence) + (2 * two_pence) + (5 * five_pence)
    print("The total amount of money you have is", total, "pence")

# Problem 6
def ten_hellos():
    count = 0
    while count < 10:
        print("Hello World")
        count = count + 1

# Problem 7
def zoom_zoom():
    number = int(input("Enter a number: "))
    count = 1
    while count <= number:
        print("zoom", count)
        count = count + 1

# Problem 8
def count_to():
    number = int(input("Enter a number: "))
    count = 1
    while count <= number:
        print(count)
        count = count + 1

# Problem 9
def count_from_to():
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))
    while start_number <= end_number:
        print(start_number)
        start_number = start_number + 1

# Problem 10
def weights_table():
    print("Kilos\tOunces")
    kilograms = 10
    while kilograms <= 100:
        ounces = kilograms * 35.273
        print(kilograms, "\t", ounces)
        kilograms = kilograms + 10

# Problem 11
def future_value():
    amount = float(input("Enter the starting investment amount: "))
    years_invested = int(input("Enter the nubmer of years it will be invested: "))
    for i in range(years_invested):
        amount = amount * 1.035
    print("The total amount after", years_invested, "years is", round(amount, 2))