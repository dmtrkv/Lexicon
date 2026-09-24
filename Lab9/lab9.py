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


# Part E - __str__

# Create a Product class with name and price.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Create one Product object and print it before defining __str__. Observe the result.
product = Product("Laptop", 999)
print(product)  # <__main__.Product object at 0x0000025D7D2C70E0>

# Add __str__ so printing the Product gives a useful human-readable description.


def __str__(self):
    return f"{self.name} costs {self.price}"


Product.__str__ = __str__

# Create at least three Product objects and print them.
products = [
    Product("Laptop", 999.99),
    Product("Phone", 699.99),
    Product("Tablet", 499.99)
]

for product in products:
    print(product)

# Use str() on one Product object, store the result in a variable and print its type.
result = str(products[0])
print(type(result))  # <class 'str'>
