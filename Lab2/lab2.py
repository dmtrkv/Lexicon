# Part A - Lists

# Create a list of at least eight programming languages. Access the first, last, third and second-to-last values.
# languages = [
#     "Python",
#     "Java",
#     "C++",
#     "JavaScript",
#     "C#",
#     "Go",
#     "Rust",
#     "Swift"
# ]

# print(languages[0])
# print(languages[-1])
# print(languages[2])
# print(languages[-2])

# # Print three different slices of the list, then print the list in reverse order using slicing.
# print(languages[::-1])

# # Use append, insert, remove and pop. After each operation, print the list so the change is visible.
# languages.append("Q")
# languages.insert(0, "A")
# languages.remove("A")
# languages.pop()
# print(languages)

# # Create a numeric list. Calculate its length, minimum, maximum and sum using built-in functions.
# numbers = [12, 5, 8, 20, 3, 15, 10]

# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# # Sort one list ascending and another descending. Explain in a comment the difference between
# # changing a list with .sort() and creating a sorted result with sorted().
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

# # Demonstrate the reference/copy issue using list_b = list_a. Then fix it with .copy().
# list_a = [1, 2, 3]
# list_b = list_a
# list_b.append(4)
# print(list_a)
# print(list_b)

# list_a = [1, 2, 3]
# list_b = list_a.copy()
# list_b.append(4)
# print(list_a)
# print(list_b)


# Part B - Tuples and unpacking

# Create a tuple representing RGB values. Unpack it into three variables and print them.
# rgb = (255, 255, 255)
# r, g, b = rgb
# print(r, g, b)

# # Create a tuple containing a person's name, age and city. Unpack and use the values in a formatted sentence.
# person = ("Alex", 25, "Stockholm")
# name, age, city = person
# print(f"{name} is {age} years old and lives in {city}.")

# # Attempt to reason about changing one tuple element.
# # Explain in a comment why tuples are useful when values should not be changed.
# # bc of constants

# # Create a list containing at least four coordinate tuples such as (10, 20). Access individual x and y values.
# list = [(1, 2), (3, 4), (5, 6), (7, 8)]
# print(f"x: {list[0][0]}, y: {list[0][1]}")

# # Part C - Sets

# # Create a list containing duplicate course names. Convert it to a set and compare the lengths before and after.
# courses = ["Python", "Java", "Python", "C++", "Java", "Python"]
# courses_set = set(courses)
# print(len(courses))
# print(len(courses_set))

# # Create two sets representing skills of two developers.
# # Find skills they share, skills only the first has, and all skills represented by either person.
# java_developer = {"Java", "Spring", "SQL"}
# python_developer = {"Python", "Django", "SQL"}
# print(java_developer & python_developer)
# print(java_developer - python_developer)
# print(java_developer | python_developer)

# # Create a set and practice add, remove/discard and membership testing.
# print('Java' in java_developer)

# # Explain in comments why a set is a better choice than a list for one real-world uniqueness problem.
# # keeps unique elements ootb, e.g. week days set

# # Part D - Dictionaries

# # Create a dictionary for a laptop with brand, model, RAM, storage and price. Read every value by key.
# laptop = {
#     "brand": "Dell",
#     "model": "XPS 15",
#     "RAM": "16GB",
#     "storage": "512GB SSD",
#     "price": 1299
# }
# print(laptop["brand"])
# print(laptop["model"])
# print(laptop["RAM"])
# print(laptop["storage"])
# print(laptop["price"])

# # Update the price, add an operating_system key and remove one key.
# laptop["price"] = 1199
# laptop["operating_system"] = "Windows 11"
# del laptop["storage"]
# print(laptop)

# # Use .get() for both an existing and a missing key. Compare it conceptually with direct indexing.
# print(laptop.get("price"))
# print(laptop.get("name"))
# # direct by missing idx -> error

# # Print keys, values and items separately.
# print(laptop.keys())
# print(laptop.values())
# print(laptop.items())

# # Create a dictionary mapping five course names to number of study hours.
# # Calculate the total hours using the dictionary values.
# courses = {
#     "Python": 10,
#     "Java": 8,
#     "SQL": 6,
#     "Git": 4,
#     "C++": 7
# }
# print(sum(courses.values()))

# # Part E - Nested collections

# # Create a list of at least five dictionaries representing books with title, author, pages and available.
# books = [
#     {"title": "Title1", "author": "Author1", "pages": 100, "available": True},
#     {"title": "Title2", "author": "Author2", "pages": 150, "available": False},
#     {"title": "Title3", "author": "Author3", "pages": 200, "available": True},
#     {"title": "Title4", "author": "Author4", "pages": 250, "available": True},
#     {"title": "Title5", "author": "Author5", "pages": 300, "available": False}
# ]

# # Access the title of the third book and the availability of the last book.
# print(books[2]["title"])
# print(books[-1]["available"])

# # Change one nested value and add a new key to one book.
# books[0]["pages"] = 120
# books[0]["genre"] = "Fiction"
# print(books)

# # Create a dictionary where each key is a department and each value is a list of employee names.
# departments = {
#     "HR": ["Employee1", "Employee2"],
#     "IT": ["Employee3", "Employee4"],
#     "Sales": ["Employee5", "Employee6"],
#     "Finance": ["Employee7", "Employee8"]
# }

# # Create a structure for three courses where each course contains a name, teacher and list of topics. 
# # Print one specific topic using chained indexing.
# courses = {
#     "course1": {
#         "name": "Course1",
#         "teacher": "Teacher1",
#         "topics": ["Topic1", "Topic2", "Topic3"]
#     }
# }
# print(courses["course1"]["topics"][1])

# # Part F - Applied challenge: Personal media catalogue

# # Create a catalogue containing at least 3 movies, games or books. 
# # Each item must be a dictionary with at least four useful fields.
# # Store all item dictionaries in one list.
# catalogue = [
#     {"title": "Movie1", "genre": "Action", "year": 2020, "rating": 8.2},
#     {"title": "Movie2", "genre": "Comedy", "year": 2021, "rating": 7.5},
#     {"title": "Movie3", "genre": "Comedy", "year": 2022, "rating": 8.7}
# ]

# # Create a set containing all unique categories/genres represented in the catalogue.
# genres = {movie["genre"] for movie in catalogue}
# print(genres)

# # Create a tuple for each item's immutable identifier plus release year, 
# # and include or associate it sensibly in your design.
# for movie in catalogue:
#     movie["id"] = (movie["title"], movie["year"])
# print(catalogue)

# # Perform at least ten manual retrieval/update operations that demonstrate nested indexing, 
# # membership and collection methods.
# print(catalogue[0].keys())
# print(catalogue[0].values())
# print(catalogue[0].items())

# # Print a clean summary of the catalogue without using loops yet. 
# # Repetition is acceptable here because loops come next lesson.
# catalogue = [
#     {"title": "Movie1", "genre": "Action", "year": 2020, "rating": 8.2},
# ]
# print(f"Title: {catalogue[0]['title']}, Genre: {catalogue[0]['genre']}, Year: {catalogue[0]['year']}, Rating: {catalogue[0]['rating']}")

# Part G - Stretch challenges

# Given two lists of usernames, determine duplicates and unique usernames using sets.
usernames_a = ["user1", "user2", "user3", "user4"]
usernames_b = ["user3", "user4", "user5", "user6"]
set_a = set(usernames_a)
set_b = set(usernames_b)
duplicates = set_a & set_b
unique_usernames = set_a | set_b
print("Duplicates:", duplicates)
print("All unique usernames:", unique_usernames)

# Design a nested collection for a small online course platform: courses, teacher, students and topics. 
# Do not write classes.
platform = {
    "courses": [
        {
            "name": "Course1",
            "teacher": "Teacher1",
            "students": ["Student1", "Student2", "Student3"],
            "topics": ["Topic1", "Topic2", "Topic3"]
        },
        {
            "name": "Course2",
            "teacher": "Teacher2",
            "students": ["Student4", "Student5", "Student6"],
            "topics": ["Topic4", "Topic5", "Topic6"]
        }
    ]
}

# Create a dictionary-based inventory for five products. 
# Update stock values manually and calculate total units using values.
inventory = {
    "Product1": 10,
    "Product2": 15,
    "Product3": 8,
    "Product4": 20,
    "Product5": 12
}
inventory["Product1"] = 14
inventory["Product3"] = 5
inventory["Product5"] = 18
total_units = sum(inventory.values())

print(inventory)
print(total_units)

# Write a short comparison in comments: list vs tuple vs set vs dictionary.
# Give one situation where each is the best fit.
# list - [] - array
# tuple - () - constant
# set - set() - unique values
# dict - {} - key/value pairs
