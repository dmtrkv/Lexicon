# Part A - Conditions

# # Write a program that classifies a number as positive, negative or zero.
# number = int(input("Write a number: "))
# print("Positive" if number > 0 else "Negative" if number < 0 else "Zero")

# # Ask for an age and classify it into at least four age groups using if/elif/else.
# age = int(input("Enter your age: "))
# if age < 13:
#     print("Child")
# elif age < 18:
#     print("Teenager")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")

# # Create a login check using a stored username and password. Both must match.
# stored_username = "admin"
# stored_password = "1234"
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username == stored_username and password == stored_password:
#     print("Login successful")
# else:
#     print("Invalid username or password")

# # Given a score from 0-100, print a grade using at least five ranges. Think carefully about condition order.
# score = int(input("Enter your score (0-100): "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# # Create a shipping rule based on order total and whether the customer is a member. Use and/or.
# order_total = 100
# member = True
# if order_total >= 50 or member:
#     print("Free shipping")
# else:
#     print("Shipping fee: $5")

# # Write five expressions using ==, !=, >, <, >= and <= and predict each boolean result before running.
# x = 10
# y = 20
# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)


# Part B - Truthy, falsy and membership

# # Create examples with empty string, non-empty string, zero, non-zero integer,
# # empty list and non-empty list. Test each directly in an if statement.
# pass

# # Ask for a language and check whether it exists in a predefined list of supported languages.
# pass

# # Create a list of blocked usernames and reject a supplied username if it appears in the list.
# pass

# # Use not to express at least two conditions in a readable way.
# is_weekend = False
# is_friday = True
# if is_weekend:
#     print('😎')
# if not is_friday:
#     print('🤓')
# else:
#     print("🥳")


# Part C - For loops

# # Loop over a list of names and print a numbered greeting for each.
# names = ["Alice", "Bob", "Charlie"]
# for i, name in enumerate(names, start=1):
#     print(f"{i}. Hello, {name}!")

# # Loop over numbers 1-50 and print only even numbers.
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# # Calculate the sum of a list manually using a loop rather than sum().
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for number in numbers:
#     total += number
# print("Sum:", total)

# # Find the largest number in a list manually without max().
# numbers = [10, 25, 7, 42, 18]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print("Largest:", largest)

# # Count how many words in a list have more than five characters.
# words = ["apple", "banana"]
# count = 0
# for word in words:
#     if len(word) > 5:
#         count += 1
# print("Words with more than five characters:", count)

# # Given a list of scores, count passes and failures using a threshold of 70.
# scores = [85, 62, 91, 55, 73, 68, 45, 100]
# passes = 0
# failures = 0
# for score in scores:
#     if score >= 70:
#         passes += 1
#     else:
#         failures += 1
# print("Passes:", passes)
# print("Failures:", failures)

# # Loop over a dictionary using keys, values and .items() in three separate examples.
# student = {
#     "name": "Max",
#     "age": 27,
#     "grade": 99
# }
# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key, value in student.items():
#     print(key, ":", value)


# Part D - range, enumerate and nested loops

# # Use range to print 10 down to 1.
# for i in range(10, 0, -1):
#     print(i)

# # Generate the multiplication table for a number supplied by the user.
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# # Use enumerate to print a playlist with track numbers starting at 1.
# playlist = ["Song A", "Song B", "Song C", "Song D"]
# for number, song in enumerate(playlist, start=1):
#     print(number, song)

# # Use nested loops to print coordinate pairs for x=1..3 and y=1..4.
# for x in range (1, 4):
#     for y in range(1, 5):
#         print(f"{x} {y}")

# # Create a simple 5x5 text grid using nested loops.
# size = 5
# symbol = 'X'
# for x in range(size):
#     row = ""
#     for y in range(size):
#         row += symbol
#     print(row)


# Part E - While loops

# # Create a countdown from 10 to 0.
# for count in range(10, -1, -1):
#     print(f"{count}!" if count > 0 else "Go!")

# # Ask repeatedly for a password until the correct password is entered.
# password = "secret"
# user_input = input("Enter your password: ")
# while user_input != password:
#     user_input = input("Enter your password: ")
# print("Logged in")

# # Create a menu that repeats until the user chooses 'quit'.
# # The menu can simply print which option was selected.
# while True:
#     print("Menu:")
#     print("1. Start")
#     print("2. Quit")
#     choice = input("Choose an option: ").lower()
#     if choice == "quit" or choice == "2":
#         print("Goodbye!")
#         break
#     else:
#         print("You selected: ", choice)

# # Ask the user for numbers until they enter 0. Keep a running total.
# pass

# # Create a guessing loop with a fixed secret number. 
# # Tell the user whether each guess is too high or too low.
# pass


# Part F - break and continue

# # Loop through numbers 1-100 and stop when you reach the first number divisible by both 7 and 9.
# pass

# # # Loop through a list of strings and skip empty strings using continue.
# pass

# # Search a list for a target name. Print 'found' and break when it appears; 
# # otherwise explain how you know it was not found.
# pass

# # Process a list of numeric values where negative values should be skipped 
# # and processing stops completely when the value 999 appears.
# numbers = [10, -5, 20, -3, 30, 999, 40, 50]
# for number in numbers:
#     if number == 999:
#         break
#     if number < 0:
#         continue
#     print(number)


# Part G - Applied challenge: Console study tracker

# # Create a list of dictionaries representing at least ten study sessions with subject and minutes.
# study_sessions = [
#     {"subject": "Python", "minutes": 90}, 
#     {"subject": "Java", "minutes": 45}, 
#     {"subject": "Python", "minutes": 45}
#     ]
# print(study_sessions)

# # Loop through the sessions and calculate total minutes.
# total_minutes = sum(session["minutes"] for session in study_sessions)
# print(total_minutes)

# # Calculate total minutes per subject using a dictionary that starts empty and is updated inside the loop.
# study_subjects = {}
# for session in study_sessions:
#     subject = session["subject"]
#     minutes = session["minutes"]  
#     if subject in study_subjects:
#         study_subjects[subject] += minutes
#     else:
#         study_subjects[subject] = minutes
# print(study_subjects)

# # Identify the longest study session without max(..., key=...).
# longest_session = study_sessions[0]
# for session in study_sessions:
#     if session["minutes"] > longest_session["minutes"]:
#         longest_session = session
# print("Longest study session:", longest_session)

# # Print only sessions longer than 45 minutes.
# for session in study_sessions:
#     if session["minutes"] > 45:
#         print(session)

# # Create a repeated menu that lets a user: view all sessions, view total time, filter by subject, or quit.
# # Use break/continue where they genuinely improve the flow.
# while True:
#     print("\nMenu:")
#     print("1. Sessions")
#     print("2. Total time")
#     print("3. Filter by subject")
#     print("4. Quit")

#     option = input("Choose an option: ")

#     if option == '4':
#         break
#     elif option == '1':
#         print(study_sessions)
#     elif option == '2':
#         print(total_minutes)
#     elif option == '3':
#         subject = input("Choose a subject: ")
#         print(study_subjects.get(subject))
#     else:
#         "Try again"

# Part H - Stretch challenges

# Print FizzBuzz from 1 to 100: multiples of 3 -> Fizz, 5 -> Buzz, both -> FizzBuzz.
pass

# # Given a sentence, count vowels without using .count() repeatedly.
# vowels = ['a', 'e', 'i', 'o' ,'u']
# sentence = "Given a sentence, count vowels without using .count() repeatedly."
# vowels_count = 0
# for letter in sentence:
#     if letter in vowels:
#         vowels_count += 1
# print(vowels_count)

# # Find all duplicate values in a list using loops and collections.
# numbers = [1, 2, 3, 3, 2, 3]
# counts = {}
# for number in numbers: # from collections import Counter -> counts = Counter(values)
#     if (counts.get(number)):
#         counts[number] += 1
#     else:
#         counts[number] = 1
# duplicates = [number for number, count in counts.items() if count > 1]
# print(duplicates)

# Build a simple text histogram: for each number in [3, 5, 2], print that many * characters.
numbers = [3, 5, 2]
for number in numbers:
    print('*' * number)
