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


# Part D - Inherited and subclass-specific behaviour

# Create a base class Employee with name and a method get_information().
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"Employee: {self.name}"

# Create Developer(Employee) and add a method that only Developer has.
class Developer(Employee):
    def write_code(self):
        return f"{self.name} is writing code"

# Create another Employee subclass of your choice and give it its own subclass-specific method.
class Tester(Employee):
    def test_code(self):
        return f"{self.name} is testing code"

# Demonstrate that both subclasses can use inherited behaviour from Employee.
developer = Developer("Bob")
tester = Tester("Ann")
print(developer.get_information())
print(developer.write_code())
print(tester.get_information())
print(tester.test_code())

# Demonstrate that an Employee object cannot automatically use a method 
# that only exists in one of its subclasses.

manager = Employee("Manager is 😴")
print(manager.get_information())
# manager.write_code() # AttributeError!
# manager.test_code() # AttributeError!
