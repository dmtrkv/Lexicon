# # Part A - Polymorphism

# # Create three classes: EmailNotification, SMSNotification and PushNotification.
# # Give all three classes a method called send(), but make each method return a different message.
# class EmailNotification:
#     def send(self):
#         return "Sending E-mail"


# class SMSNotification:
#     def send(self):
#         return "Sending SMS"


# class PushNotification:
#     def send(self):
#         return "Sending Push Notification"


# # Create one object from each class and store them in the same list.
# notifications = [EmailNotification(),
#                  SMSNotification(),
#                  PushNotification()]

# # Loop through the list and call send() on every object.
# for notification in notifications:
#     print(notification.send())

# # In a comment, explain why the loop does not need to know the exact class of each object.
# # It's bc of polymorphism


# # Part B - Polymorphism with inheritance

# # Create a base class Document with a title attribute and a method describe().
# class Document:
#     def __init__(self, title):
#         self.title = title

#     def describe(self):
#         pass

# # Create PDFDocument(Document) and TextDocument(Document).
# # Override describe() in both subclasses so they return different descriptions.


# class PDFDocument(Document):
#     def describe(self):
#         return f"PDF document: {self.title}.pdf"


# class TextDocument(Document):
#     def describe(self):
#         return f"Text document: {self.title}.doc"


# # Create several PDFDocument and TextDocument objects and store them in one list.
# documents = [
#     PDFDocument("Invoice"),
#     TextDocument("Report"),
# ]

# # Loop through the list and print each document's title and the result of describe().
# for document in documents:
#     print(document.title)
#     print(document.describe())


# # Part C - Duck typing

# # Create two unrelated classes, for example Printer and Screen. Do not use inheritance between them.
# # Give both classes a method called display_status().
# class Printer:
#     def display_status(self):
#         print("Off")

# class Screen:
#     def display_status(self):
#         print("On")

# # Create objects from both classes and store them in the same list.
# devices = [
#     Printer(),
#     Screen()
# ]

# # Loop through the list and call display_status() on each object.
# for device in devices:
#     device.display_status()

# # In a comment, explain why this works even though the classes do not share a base class.
# # Python cares about what an object can do, not what its type is
# # (walks & quacks like a duck -> it's a duck)


# # Part D - isinstance()

# # Create a base class User and a subclass AdminUser(User).
# class User:
#     pass


# class AdminUser(User):
#     is_admin = True
#     pass


# # Create an AdminUser object.
# admin = AdminUser()

# # Use isinstance() to check whether the object is an AdminUser, a User and a string.
# assert isinstance(admin, AdminUser)
# assert isinstance(admin, User)
# assert not isinstance(admin, str)

# # Print all three results.
# pass

# # In a comment, explain why the AdminUser object is also considered an instance of User.
# # AdminUser extends User so 'admin' is a user


# # Part E - __str__

# # Create a Product class with name and price.
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# # Create one Product object and print it before defining __str__. Observe the result.
# product = Product("Laptop", 999)
# print(product)  # <__main__.Product object at 0x0000025D7D2C70E0>

# # Add __str__ so printing the Product gives a useful human-readable description.


# def __str__(self):
#     return f"{self.name} costs {self.price}"


# Product.__str__ = __str__

# # Create at least three Product objects and print them.
# products = [
#     Product("Laptop", 999.99),
#     Product("Phone", 699.99),
#     Product("Tablet", 499.99)
# ]

# for product in products:
#     print(product)

# # Use str() on one Product object, store the result in a variable and print its type.
# result = str(products[0])
# print(type(result))  # <class 'str'>


# # Part F - __str__ with inheritance

# # Create a base class Account with owner and balance.
# # Add __str__ to Account.
# class Account:
#     def __init__(self, owner, balance=0.00):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self) -> str:
#         return f"{self.owner}: {self.balance:.2f}"

# # Create SavingsAccount(Account) with an additional interest_rate attribute. Use super() in __init__.
# # Override __str__ in SavingsAccount so its output also includes the interest rate.


# class SavingsAccount(Account):
#     def __init__(self, owner, balance=0.00, interest_rate=0.00):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def __str__(self) -> str:
#         return super().__str__() + f" (interest rate: {self.interest_rate:.2f}%)"


# # Create and print both an Account and a SavingsAccount object.
# account = Account("Ann", 200_000)
# saving_account = SavingsAccount("Bob", 100000.00, 5.00)
# print(account)
# print(saving_account)


# # Part G - Inheritance or composition?

# # Create CPU with a model attribute.
# class CPU:
#     def __init__(self, model):
#         self.model = model

# # Create Computer with brand and a CPU object. Use composition, not inheritance.
# class Computer:
#     def __init__(self, brand, cpu):
#         self.brand = brand
#         self.cpu = cpu

# # Create a CPU object and pass it to a Computer object.
# cpu = CPU("Intel Core i3")
# computer = Computer("ASUS", cpu)

# # Print the computer brand and CPU model through the Computer object.
# print(computer.brand)
# print(computer.cpu.model)

# # In comments, explain why "Computer HAS-A CPU" makes more sense than "Computer IS-A CPU".
# # CPU is just a part of PC, so the relationship should be HAS-A

# # For each pair below, write whether you would most likely use inheritance (IS-A) or composition (HAS-A):
# # Car / Engine - HAS-A
# # Manager / Employee - IS-A
# # Course / Teacher - HAS-A
# # Phone / Device - IS-A


# Part H - Applied challenge: Export system

# Build a small export system using the concepts from today's lesson.
# Create a base class Exporter with a method export(data).
class Exporter:
    def export(self, data):
        pass

    def __str__(self) -> str:
        return ">>> "

# Create at least three subclasses, for example ConsoleExporter, TextExporter and SummaryExporter.
# Override export(data) in every subclass so each handles the same data differently.
# You do not need to create real files.
# Add a useful __str__ method to the exporter classes.


class ConsoleExporter(Exporter):
    def export(self, data):
        print(f"Console: {data}")

    def __str__(self) -> str:
        return super().__str__() + "Console Exporter: "


class TextExporter(Exporter):
    def export(self, data):
        print(f"Text: {data}")

    def __str__(self) -> str:
        return super().__str__() + "Text Exporter: "


class SummaryExporter(Exporter):
    def export(self, data):
        print(f"Summary: {data}")

    def __str__(self) -> str:
        return super().__str__() + "Summary Exporter: "


# Create several exporter objects and store them in one list.
exporters = [ConsoleExporter(), TextExporter(), SummaryExporter()]

# Loop through the list and call export() on each object to demonstrate polymorphism.
for exporter in exporters:
    exporter.export("data")

# Create one additional class that is not part of the Exporter inheritance hierarchy
# but still provides an export(data) method. Show that it can be used by the same calling code.


class GoodsExporter():
    def __init__(self, country) -> None:
        self.country = country

    def export(self, goods):
        print(f"'{goods}' goods are exported to: {self.country}")


exporters.append(GoodsExporter("Canada"))
for exporter in exporters:
    exporter.export("data")

# Use isinstance() at least once to inspect a meaningful type relationship.
for exporter in exporters:
    if isinstance(exporter, GoodsExporter):
        print(exporter.country)

# Add one example of composition to the program and explain the HAS-A relationship in a comment.


class FileProcessor:
    def __init__(self, exporter) -> None:
        # File Processor is not an exporter, but it has one to export files
        self.exporter = exporter

    def process_file(self, file):
        print(f"Processing file: {file}")
        self.exporter.export(file)
        print(f"File processed")


file_processor = FileProcessor(TextExporter())
file_processor.process_file("lab9.txt")
