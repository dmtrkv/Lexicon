# # Part A - Classes and objects

# # Create a Book class with title, author and pages.
# # Create at least four Book objects and print their attributes.
# class Book:
#     def __init__(self, title, author, pages) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages


# Book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
# pass

# print(f"Book 1: {Book1.title} by {Book1.author}, {Book1.pages} pages")
# pass

# # Create a Laptop class with brand, model, ram_gb and price.
# # Create three separate objects and change the price of one object.


# class Laptop:
#     def __init__(self, brand, model, ram_gb, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# Laptop1 = Laptop("Dell", "XPS 13", 16, 999.99)
# Laptop2 = Laptop("Apple", "MacBook Air", 8, 1099.99)


# Laptop1.price = 899.99
# print(
#     f"Laptop 1: {Laptop1.brand} {Laptop1.model}, {Laptop1.ram_gb}GB RAM, ${Laptop1.price}")
# print(
#     f"Laptop 2: {Laptop2.brand} {Laptop2.model}, {Laptop2.ram_gb}GB RAM, ${Laptop2.price}")

# # Create two objects with the same attribute values.
# # Use is to check whether they are the same object.
# Laptop3 = Laptop("Dell", "XPS 13", 16, 999.99)
# print(f"Are Laptop1 and Laptop3 the same object? {Laptop1 is Laptop3}")

# # Add a default value to at least one __init__ parameter.


# class Smartphone:
#     def __init__(self, brand, ram_gb=4, price=499.99) -> None:
#         self.brand = brand
#         self.ram_gb = ram_gb
#         self.price = price


# # Create one object using keyword arguments.
# Smartphone1 = Smartphone(brand="Samsung", ram_gb=8)
# print(
#     f"Smartphone 1: {Smartphone1.brand}, {Smartphone1.ram_gb}GB RAM, ${Smartphone1.price}")


# # Part B - Methods and state

# # Extend your Book class with an is_long() method that returns True if the book has more than 300 pages.
# class Book:
#     def __init__(self, pages) -> None:
#         self.pages = pages

#     def is_long(self):
#         return self.pages > 300


# book = Book(301)
# print(book.is_long())

# # Create a BankAccount class with owner and balance. Add a deposit() method that changes the balance.


# class BankAccount:
#     def __init__(self, balance) -> None:
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

# # Add a withdraw() method. Prevent withdrawals that would make the balance negative by raising a ValueError.
#     def withdraw(self, amount):
#         if (amount > self.balance):
#             raise ValueError("Insufficient balance!")
#         self.balance -= amount


# # Create a Task class with title and completed=False. Add complete() and reopen() methods.
# pass

# # Create at least two objects from one of your classes and show
# # that changing the state of one object does not change the other.
# account1 = BankAccount(200)
# account2 = BankAccount(100)
# account2.withdraw(100)
# assert account2.balance == 0
# assert account1.balance == 200


# # Part C - Instance and class attributes

# # Create a Product class with name and price as instance attributes.
# class Product:
#     tax_rate = .25

#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price


# # Add a class attribute called tax_rate that is shared by all Product objects.
# p1 = Product("p1", 10)
# p2 = Product("p2", 20)
# assert p1.tax_rate == p2.tax_rate

# # Add a price_with_tax() method that returns the price including tax.
# pass

# # Create at least three Product objects and print their prices with tax.
# pass

# # Change Product.tax_rate and show how it affects the Product objects.
# assert p1.tax_rate == .25
# assert p2.tax_rate == .25
# Product.tax_rate = .35
# assert p1.tax_rate == .35
# assert p2.tax_rate == .35

# # Give one Product object its own tax_rate. Print the tax rate from that object,
# # another Product object and the Product class.
# p1.tax_rate = .15
# assert p1.tax_rate == .15
# assert p2.tax_rate == .35
# assert Product.tax_rate == .35


# Part D - Collections of objects

# Create at least six Student objects with name and score.
# Add a get_status() method that returns "PASS" or "FAIL" based on the score.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return "PASS" if self.score > 70 else "FAIL"


# Store all Student objects in a list.
students = [
    Student("Ann", 99),
    Student("Bob", 85),
    Student("Charlie", 78),
    Student("Diana", 95),
    Student("Ethan", 88),
    Student("Fiona", 61)
]

# Loop through the list and print each student's name and score.
pass

# Loop through the students again and print each student's name and status.
for student in students:
    print(f"{student.name}: {student.get_status()}")

# Use a list comprehension to create a new list containing only students with a score of 70 or higher.
print([student.name for student in students if student.score >= 70])


# Part E - Objects inside objects

# Create a Teacher class with a name.
class Teacher:
    def __init__(self, name):
        self.name = name

# Create a Course class with a course name and a teacher. The teacher should be a Teacher object.
# Extend Course so that it also contains an initially empty list of Student objects.
# Add an add_student() method and use it to add at least three Student objects to the course.


class Course:

    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Create a Teacher object and use it when creating a Course object.
teacher = Teacher("Mr. Smith")
course = Course("Python Programming", teacher)

# Print the course name and the teacher's name through the Course object.
print(course.teacher.name)

course.add_student(students[0])
course.add_student(students[1])

# Loop through course.students and print the name of every student.
for student in course.students:
    print(student.name)
