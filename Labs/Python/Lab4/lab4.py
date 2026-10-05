# # Part A - Function fundamentals

# # Write functions greet(), show_course_name() and print_separator(). Call each more than once.
# def greet():
#     print("Hello")
#     print_separator()
#     show_course_name()


# def show_course_name():
#     print("Python + AI")


# def print_separator():
#     print('-----')


# greet()

# # Write greet_person(name) and introduce(name, city).
# pass

# # Write add(a, b), subtract(a, b), multiply(a, b) and divide(a, b). Each must return a value.
# pass

# # Demonstrate parameter vs argument in comments using one of your functions.


# def func(parameter):
#     pass


# argument = 1
# func(argument)

# # Create calculate_area(width, height)
# # and use its returned value in another calculation.
# def calculate_area(width, length):
#     return width * length


# def calulate_volume(width, length, height):
#     return calculate_area(width, length) * height


# print(f"Volume: {calulate_volume(10, 10, 10)}")


# # Part B - Return values

# # Write is_even(number) returning True/False.
# pass

# # Write get_larger(a, b) returning the larger value without max().


# def get_larger(a, b):
#     return a if a > b else b
# print(get_larger(1, 1.1))

# # Write classify_score(score) returning PASS or FAIL.
# pass

# # Write full_name(first_name, last_name) returning a formatted string.
# pass

# # Write calculate_discount(price, percent) returning the discounted price.
# def calculate_discount(price, percent):
#     return price * percent / 100
# print(calculate_discount(100.00, 20))

# # Show with a small example why print(result) inside a function is not the same as return result.
# def print_func():
#     print("Inside a function")

# if not print(print_func()):
#     print("print_func() returns 'None'")


# # Part C - Defaults and keyword arguments

# # Create greet(name, greeting='Hello'). Test positional and keyword arguments.
# def greet(name, greeting='Hello'):
#     print(f"{greeting} {name}!")
# greet("Max")
# greet("Max", "Hi")

# # Create calculate_price(price, quantity=1, discount=0). Return the final total.
# pass

# # Create create_profile(name, city='Unknown', active=True) returning a dictionary.
# def create_profile(name, city='Unknown', active=True):
#     profile = {}
#     profile["name"] = name
#     profile["city"] = city
#     profile["active"] = active
#     return profile


# print(create_profile("Max"))

# # Call one function using keyword arguments in a different order from the parameter definition.


# def sum(a, b):
#     print(f"{a} + {b}")
#     return a + b


# print(sum(b=2, a=1))

# # Write one invalid default-parameter ordering as a comment and explain why it is invalid.
# def invalid_func(default=1, param): # Non-default argument follows default argument
#     pass


# # Part D - Functions and collections

# # Write calculate_total(numbers) manually using a loop.
# pass

# # Write count_even(numbers).
# def count_even(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 == 0:
#             count += 1
#     return count

# def count_even_py(numbers):
#     return sum(number % 2 == 0 for number in numbers)


# # print(count_even([1, 2, 3, 4, 5]))

# # Write get_long_words(words, minimum_length) returning a new list.
# def get_long_words(words, minimum_length):
#     return [word for word in words if len(word) >= minimum_length]


# print(get_long_words(["one", "two", "three"], 5))

# # Write find_student(students, name) where students is a list of dictionaries.
# # Return the matching dictionary or None.
# def find_student(students, name):
#     for student in students:
#         if student["name"] == name:
#             return student
#     return None


# students = [{"name": "Max"}, {"name": "Bob"}]
# print(find_student(students, "Max"))
# print(find_student(students, "Xam"))

# # Write average_score(students) for a list of dictionaries containing score values.
# pass

# # Write get_active_users(users) returning only dictionaries where active is True.
# def get_active_users(users):
#     return [user for user in users if user["active"]]


# users = [{"name": "Max", "active": True}, {"name": "Bob", "active": False}]
# print(get_active_users(users))


# Part E - Decomposition

# # Build a temperature report using separate functions for Celsius-to-Fahrenheit conversion,
# # classification ('cold/warm/hot') and formatting.
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9 / 5) + 32


# def classify_temperature(celsius):
#     if celsius < 10:
#         return "cold"
#     elif celsius < 25:
#         return "warm"
#     else:
#         return "hot"


# def format_temperature_report(celsius):
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     classification = classify_temperature(celsius)

#     return f"{celsius}C = {fahrenheit}F ({classification})"


# print(format_temperature_report(20))

# # Build a small order calculation using separate functions for subtotal, discount and final total.
# def calculate_subtotal(items):
#     subtotal = 0
#     for item in items:
#         subtotal += item["price"] * item["quantity"]
#     return subtotal


# def calculate_discount(subtotal, discount=0.0):
#     return subtotal * discount / 100


# def calculate_total(items, discount=0.0):
#     subtotal = calculate_subtotal(items)
#     discount = calculate_discount(subtotal, discount)
#     return subtotal - discount


# assert calculate_total([{"price": 10, "quantity": 1}, {
#                        "price": 20, "quantity": 2}]) == 50
# assert calculate_total([{"price": 10, "quantity": 1}, {
#                        "price": 20, "quantity": 2}], 10.0) == 45

# # Refactor one earlier exercise that contains repeated code into at least three functions.
# def print_line():
#     print('\n')


# def print_stars(stars):
#     print('*' * stars)


# def print_param(param):
#     print(f"Parameter: {param}")


# # Write a main-like section at the bottom of the file that calls your functions in a clear sequence.
# if __name__ == "__main__":
#     print_stars(5)
#     print_line()
#     print_param("from main")
#     print_line()
#     print_stars(5)


# # Part F - Applied challenge: Event registration processor

# # Create functions to normalize a participant name,
# # validate an age range using boolean return values,
# # calculate a registration fee based on age/student status,
# # and create a participant dictionary.
# def normalize_name(name):
#     return name.strip().title()


# def validate_age(age):
#     return 18 <= age <= 65


# def calculate_registration_fee(age, is_student):
#     if is_student:
#         return 50
#     elif age < 30:
#         return 75
#     else:
#         return 100


# def create_participant(name, age, is_student):
#     return {
#         "name": normalize_name(name),
#         "age": age,
#         "student": is_student,
#         "fee": calculate_registration_fee(age, is_student)
#     }


# # Create at least eight participant dictionaries using your functions.
# participants = [
#     create_participant("Alice Johnson", 22, True),
#     create_participant("Bob Smith", 35, False),
#     create_participant("Charlie Brown", 28, False),
#     create_participant("Diana Wilson", 19, True),
#     create_participant("Ethan Davis", 45, False),
#     create_participant("Fiona Miller", 30, True),
#     create_participant("George Moore", 25, False),
#     create_participant("Hannah Taylor", 60, False)
# ]

# # Write a function that receives the participant list and returns the total expected registration revenue.


# def total_revenue(participants):
#     return sum(participant["fee"] for participant in participants)


# assert (total_revenue(participants)) == 600


# # Write a function that returns only student participants.
# def get_students(participants):
#     return [participant for participant in participants if participant["student"]]


# print(get_students(participants))

# # Write a function that returns the oldest participant.


# def get_age(participant):
#     return participant["age"]


# def get_oldest_participant(participants):
#     return max(participants, key=get_age)


# print(f"Oldest: {get_oldest_participant(participants)}")

# # Write a function that creates a readable summary string for one participant.


# def participant_summary(participant):
#     return f"{participant['name']} is {participant['age']} and pays ${participant['fee']} fee."


# for participant in participants:
#     print(participant_summary(participant))

# # Keep input/output responsibilities separate from calculation functions as much as possible.
# pass


# Part G - Stretch challenges

# Write a function that returns both minimum and maximum from a list without min()/max(). Return two values.
def get_min_max(numbers):
    minimum = maximum = numbers[0]
    for number in numbers:
        minimum = number if number < minimum else minimum
        maximum = number if number > maximum else maximum

    return minimum, maximum


print(get_min_max([1, 2, 3, 4, 5]))

# Write a function that checks whether a word is a palindrome.


def is_palindrom(word):
    return word == word[::-1]


assert is_palindrom("bob") == True
assert is_palindrom("ace") == False

# Write a function that counts character frequencies and returns a dictionary.


def count_characters(text):
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    return count


print(count_characters(
    "Write a function that counts character frequencies and returns a dictionary."))

# Write a function that receives a list of numbers and returns a new dictionary with keys positive,
# negative and zero containing counts.


def count_numbers(numbers):
    counts = {
        "positive": 0,
        "negative": 0,
        "zero": 0
    }

    for number in numbers:
        if number > 0:
            counts["positive"] += 1
        elif number < 0:
            counts["negative"] += 1
        else:
            counts["zero"] += 1

    return counts


result = count_numbers([-1, 0, 1])
assert result["positive"] == 1
assert result["negative"] == 1
assert result["zero"] == 1

# Add light type hints and a short docstring to at least five functions.


def func(param1: int, param2: int) -> int:
    """This is smaple docstring"""
    pass
