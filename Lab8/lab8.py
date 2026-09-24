# # Part A - Mutable default arguments

# # Create a BadTeam class with name and a default parameter members=[]. Add an add_member() method.
# class BadTeam:
#     def __init__(self, name, members=[]) -> None:
#         self.name = name
#         self.members = members

#     def add_member(self, member):
#         self.members.append(member)


# # Create two BadTeam objects without providing a members list.
# # Add a member to only one team and print both lists. Explain in a comment what happened.
# team1 = BadTeam("Team 1")
# team2 = BadTeam("Team 2")

# team1.add_member("Ann")

# # Both teams contain "Ann" because the members[] is shared
# print(team1.members)  # ['Ann']
# print(team2.members)  # ['Ann'] !!!

# # Create a corrected Team class using None as the default value and create a new list inside __init__.


# class GoodTeam:
#     def __init__(self, name, members=None) -> None:
#         self.name = name
#         if members is None:
#             self.members = []
#         else:
#             self.members = members

#     def add_member(self, member):
#         self.members.append(member)


# # Repeat the test with two Team objects and show that each object now has its own list.
# team1 = GoodTeam("Team 1")
# team2 = GoodTeam("Team 2")

# team1.add_member("Bob")

# print(team1.members)  # ['Bob']
# print(team2.members)  # []


# # Part B - Dictionary or class?

# # Represent a movie using a dictionary with title, director and rating.
# movie = {
#     "title": "Inception",
#     "director": "Christopher Nolan",
#     "rating": 8.8
# }

# # Represent the same information using a Movie class.
# # Add a method to Movie that returns whether the movie is highly rated.
# # Choose a sensible rating threshold.


# class Movie:
#     def __init__(self, title, director, rating) -> None:
#         self.title = title
#         self.director = director
#         self.rating = rating

#     def is_highly_rated(self):
#         return self.rating > 80

# # In comments, briefly explain one situation where you would choose a dictionary
# # and one where you would choose a class.

# # dict - just key/value pairs
# # class - fields + methods (like is_highly_rated())


# # Part C - Inheritance fundamentals

# # Create a base class Account with owner and balance.
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

# # Create SavingsAccount(Account) with an additional interest_rate attribute.
# # Use super() so SavingsAccount reuses the initialization from Account.


# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate


# # Create at least two objects and print their attributes.
# account1 = Account("Ann", 1000)
# account2 = SavingsAccount("Bob", 2000, 0.05)

# print(account1.owner, account1.balance)
# print(account2.owner, account2.balance, account2.interest_rate)

# # Write the "is-a" statement that explains why this inheritance relationship makes sense.
# print(f"{account2.interest_rate}" if account2.__class__ is SavingsAccount
#       else "Only saving account can have an interest rate")


# # Part D - Inherited and subclass-specific behaviour

# # Create a base class Employee with name and a method get_information().
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def get_information(self):
#         return f"Employee: {self.name}"

# # Create Developer(Employee) and add a method that only Developer has.
# class Developer(Employee):
#     def write_code(self):
#         return f"{self.name} is writing code"

# # Create another Employee subclass of your choice and give it its own subclass-specific method.
# class Tester(Employee):
#     def test_code(self):
#         return f"{self.name} is testing code"

# # Demonstrate that both subclasses can use inherited behaviour from Employee.
# developer = Developer("Bob")
# tester = Tester("Ann")
# print(developer.get_information())
# print(developer.write_code())
# print(tester.get_information())
# print(tester.test_code())

# # Demonstrate that an Employee object cannot automatically use a method
# # that only exists in one of its subclasses.

# manager = Employee("Manager is 😴")
# print(manager.get_information())
# # manager.write_code() # AttributeError!
# # manager.test_code() # AttributeError!


# # Part E - super() and shared initialization

# # Create a base class Device with brand and year.
# # class Device:
# #     def __init__(self, brand, year) -> None:
# #         self.brand = brand
# #         self.year = year

# # Add useful shared initialization logic inside Device,
# # for example validation that year cannot be negative and an attribute such as is_active=True.
# class Device:
#     def __init__(self, brand, year) -> None:
#         if year < 0:
#             raise ValueError("Year cannot be negative")

#         self.brand = brand
#         self.year = year
#         self.is_active = True

# # Create Laptop(Device) with one additional attribute such as ram_gb. Use super().
# class Laptop(Device):
#     def __init__(self, brand, year, ram_gb) -> None:
#         super().__init__(brand, year)
#         self.ram_gb = ram_gb

# # Create another Device subclass with its own additional attribute and use super() again.
# class Phone(Device):
#     def __init__(self, brand, year, storage_gb) -> None:
#         super().__init__(brand, year)
#         self.storage_gb = storage_gb

# # Demonstrate that both subclasses receive the shared initialization logic
# # from Device without duplicating it.
# laptop = Laptop("Dell", 2024, 16)
# phone = Phone("Samsung", 2023, 256)

# print(laptop.brand)
# print(laptop.year)
# print(laptop.is_active)
# print(laptop.ram_gb)

# print(phone.brand)
# print(phone.year)
# print(phone.is_active)
# print(phone.storage_gb)


# # Part F - Method overriding

# # Create a base class Notification with a method send() that returns a general message.
# class Notification:
#     def send(self):
#         return "Sending notification"

# # Create EmailNotification(Notification) and SMSNotification(Notification).
# # Override send() in both subclasses so each returns a different message.


# class EmailNotification(Notification):
#     def send(self):
#         return "Sending E-mail notification"


# class SMSNotification(Notification):
#     def send(self):
#         return "Sending SMS notification"


# # Create one object from each class and call send() on all of them.
# notification = Notification()
# email = EmailNotification()
# sms = SMSNotification()

# print(notification.send())
# print(email.send())
# print(sms.send())

# # Explain in a comment which method is used when send() is called on each object.
# # Each object calls its class-specific method


# # Part G - Override and still use the base method

# # Create a base class Report with a method get_summary() that returns a general report summary.
# class Report:
#     def get_summary(self):
#         return "General report summary"

# # Create SalesReport(Report) and override get_summary().
# # class SalesReport(Report):
# #     def get_summary(self):
# #         return "Sales report summary"

# # Inside the overridden method, call the base implementation using super()
# # and add SalesReport-specific information.
# class SalesReport(Report):
#     def get_summary(self):
#         return super().get_summary() + " with sales data"

# # Create a SalesReport object and print the final result.
# report = SalesReport()
# print(report.get_summary())


# Part H - Applied challenge: User accounts

# Build a small user account system using inheritance.
# Create a base class User with at least username and email.
# Add a useful method to User that all user types should inherit.
# Create AdminUser(User) and PremiumUser(User).
# Give each subclass at least one additional attribute and one subclass-specific method.
# Use super() in both subclasses instead of duplicating User's initialization.
# Add one method to User and override it differently in AdminUser and PremiumUser.
# In one overridden method, use super() to reuse the base implementation and then extend it.
# Create several objects and demonstrate inherited methods, subclass-specific methods and overridden methods.
# Add at least one sensible validation using ValueError.
# In comments, explain why AdminUser and PremiumUser have an "is-a" relationship with User.
class User:
    def __init__(self, username, email):
        if not username or not email:
            raise ValueError("Username or E-mail cannot be empty")

        self.username = username
        self.email = email

    def get_info(self):
        return f"Username: {self.username}, Email: {self.email}"

    def get_role(self):
        return "Regular user"


class AdminUser(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    def manage_users(self):
        return f"{self.username} can manage users"

    def get_role(self):
        return super().get_role() + " with admin privileges"


class PremiumUser(User):
    def __init__(self, username, email, subscription):
        super().__init__(username, email)
        self.subscription = subscription

    def access_premium_content(self):
        return f"{self.username} can access premium content"

    def get_role(self):
        return "Premium user"


user = User("ann", "ann@example.com")
admin = AdminUser("bob", "bob@example.com",
                  ["create", "read", "update", "delete"])
premium = PremiumUser("cia", "cia@example.com", "Gold")

print(user.get_info())
print(user.get_role())

print(admin.get_info())
print(admin.get_role())
print(admin.manage_users())
assert isinstance(admin, User) # IS-A relationship bc Admin is a User (with permissions)

print(premium.get_info())
print(premium.get_role())
print(premium.access_premium_content())
assert isinstance(premium, User)  # IS-A relationship bc Premium User is a User (with privileges)
