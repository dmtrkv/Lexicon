# PART A
# A.1
print("Dmitri")
print("Python + AI")
print("Python basics")

# A.2
name = "Max"
age = 30
height_meters = 1.80
is_student = True
# print(name, type(name))
# print(age, type(age))
# print(height_meters, type(height_meters))
# print(is_student, type(is_student))

# A.3
# print(type(name))
name = 30
# print(type(name))  # dynamic typing

# A.4
first_number = 10
second_number = 2
# print("First number:", first_number)
# print("Second number:", second_number)
# print("Addition:", first_number + second_number)
# print("Subtraction:", first_number - second_number)
# print("Multiplication:", first_number * second_number)
# print("Division:", first_number / second_number)
# print("Floor division:", first_number // second_number)
# print("Remainder:", first_number % second_number)
# print("Exponentiation:", first_number ** second_number)

# A.5
# string to int
a = "27"
b = "3"
# print(int(a) + int(b))  # 30 not "273"

# int to float
# print(f"{5 / 2}") # conversion to floating point

# number to string
age = 29
# print("Max is " + str(age))  # avoids type error

# PART B
# B.1


def calculate_age(current_year):
    name = input("What's your name? ")
    birth_year = int(input("What is your birth year? "))
    print(f"{name}, your approximate age is: {current_year - birth_year}")


# calculate_age(2026)

# B.2
def calculate_final_price():
    price = float(input("What is the price? "))
    discount = float(input("What is the discount %? "))
    final_price = price - (price * discount / 100)
    print(
        f"Final price after {discount}% discount is: ${final_price:.2f}")


# calculate_final_price ()

# B.3
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {celsius * 9 / 5 + 32}")

# celsius_to_fahrenheit()

# B.4


def calculate_room():
    room_length = float(input("Enter room length: "))
    room_width = float(input("Enter room width: "))

    room_area = room_length * room_width
    room_perimeter = 2 * (room_length + room_width)

    print(f"Area: {room_area}")
    print(f"Perimeter: {room_perimeter}")

# calculate_room()

# B.5


def dangerous_function():
    print(int(input("What is your age? ")))  # ValueError if not integer

# dangerous_function()

# PART C
# C.1


def process_sentence(sentence):
    print(f"Length: {len(sentence)}")
    print(f"Uppercase: {sentence.upper()}")
    print(f"Lowercase: {sentence.lower()}")
    print(f"Trimmed: {sentence.strip()}")

# process_sentence("  Python programming language.  ")

# C.2


def full_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = f"{first_name} {last_name}"

    print(f"Full name: {full_name}")

# full_name()


# C.3
# Given the string 'python programming', print the first character, last character,
# first six characters, last eleven characters and the entire string reversed.
str = 'Python programminG'
# print(str[0])
# print(str[-1])
# print(str[:6])
# print(str[-11:])
# print(str[::-1])

# C.4


def create_username():
    first_name = input("Enter your first name: ").strip().lower()
    last_name = input("Enter your last name: ").strip().lower()

    username = f"{first_name[:3]}{last_name[:5]}"

    print(f"Username: '{username}'")

# create_username()

# C.5


def split_email(email):
    print(email)
    print(f"Name: {email.split('@')[0]}")
    print(f"Domain: {email.split('@')[1]}")

# split_email("x@y.z")


# C.6
sentence = "X Programming Language"
# print(sentence)
sentence = sentence.replace('X', 'Python')
# print(sentence)

# Part D - String investigation

# D.1
# Predict the output of at least eight expressions using indexing and slicing before running them.
# Include positive indexes, negative indexes, omitted start/end values and a step.
str = 'abc'
# a
# print(str[0])
# c
# print(str[-1])
# abc
# print(str[:3])
# bc
# print(str[-2:])
# cba
# print(str[::-1])
# ac
# print(str[::2])
#
# print(str[1:1])
# a
# print(str[-3::-1])

# D.2
str = 'Artificial Intelligence'
# First 10 characters: 'Artificial'
# print(str[0:10])
# # Characters from index 11: 'Intelligence'
# print(str[11:])
# # First 5 characters: 'Artif'
# print(str[:5])
# # Last 5 characters: 'gence'
# print(str[-5:])
# # Every second character: 'Atfca neligne'
# print(str[::2])
# # Reverse order
# print(str[::-1])

# D.3
# Investigate the difference between .split(), .strip(), .replace() and the in operator.
# Write one useful example of each.
# print("a,b,c".split(',')) # list
# print(" abc   ".strip()) # "abc"
# print("abc".replace("abc", "def")) # "def"
# print("str" in "str") # True

# D.4
str = "immutable"
# str[0] = "!" # TypeError: 'str' object does not support item assignment
str = '!' + str[1:]
# print(str)

# Part E - Applied challenge: Registration summary


# first_name = input("Enter your first name: ").strip()
# last_name = input("Enter your last name: ").strip()
# city = input("Enter your city: ").strip()
# year_of_birth = input("Enter your year of birth: ").strip()
# favourite_language = input("Enter your favourite programming language: ").strip()

# user_id = first_name[:3] + last_name[:3] + year_of_birth
# full_name = first_name + " " + last_name
# initials = first_name[0].upper() + last_name[0].upper()
# name_length = len(full_name.replace(" ", ""))
# reversed_language = favourite_language[::-1]
# city_initial = city[0].upper()
# language_short = favourite_language[:3]
# contains_a = 'a' in favourite_language.lower()
# last_name_last_letter = last_name[-1]

# print(f"Full Name:              {full_name}")
# print(f"City:                   {city}")
# print(f"Year of Birth:          {year_of_birth}")
# print(f"Favourite Language:     {favourite_language}")
# print(f"Generated User ID:      {user_id}")
# print("-" * 35)

# Part F - Stretch challenges Python Foundation

# Create a simple seconds converter: input total seconds and calculate whole hours,
# remaining minutes and remaining seconds using // and %.
total_seconds = 3666
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# print(f"{total_seconds}s = {hours}h:{minutes}m:{seconds}s")

# Given a four-digit integer, extract and print each digit without converting the number to a string.
integer = 5678
# print(integer)

thousands = integer // 1000
digit = integer % 1000

hundreds = digit // 100
digit = digit % 100

tens = digit // 10
digit = digit % 10

# print(f"{thousands} {hundreds} {tens} {digit}")

# Create a text masking program that displays only the first two and last two characters
# of a supplied word, replacing the middle with * characters.
word = "masking"
print(f"{word[:2]}{(len(word) - 4) * '*'}{word[-2:]}")
