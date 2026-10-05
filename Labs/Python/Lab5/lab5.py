# # Part A - Scope

# # Create a global variable course_name and a function that creates a local variable with the same name.
# # Print both and explain the result.
# course_name = "global"


# def func():
#     course_name = "local"
#     print(course_name)  # prints 'local' bc of the local scope


# func()

# def func():
#     global course_name
#     course_name = "local"

# func()
# print(course_name) # local

# # Create a function with a local counter and show that it does not remain available outside the function.
# pass

# # Create a function that attempts to modify a global numeric variable without global.
# # Observe/describe the problem, then rewrite the design to return the new value instead.


# def func():
#     # course_name = "Python + AI" # no effect on global 'course_name'
#     return "Python + AI"


# course_name = func()
# print(course_name)

# # Create a nested function and demonstrate a simple enclosing-scope lookup.


# def func1():
#     text = "enclosing"
#     print(text)

#     def func2():
#         nonlocal text
#         text = "local"
#         print(text)
#     func2()
#     print(text)  # local


# func1()

# # Create examples that avoid shadowing built-ins such as list, str, sum and max.
# list = [1, 2, 3]
# # print(list("abc"))  # TypeError: 'list' object is not callable
# numbers = [1, 2, 3]
# print(numbers)


# # Part B - *args

# # Write add_all(*numbers) returning the sum without sum().


# def add_all(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total


# assert add_all(1, 2, 3) == 6

# # Write average(*numbers). Decide what should happen when no numbers are supplied.


# def average(*numbers):
#     if not numbers:
#         raise ValueError("At least one number is required")
#     return add_all(*numbers) / len(numbers)


# assert average(1, 2, 3) == 2

# # Write longest_word(*words) returning the longest word.


# def longest_word(*words):
#     longest = ''
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest
#     # return max(words, key=len)


# assert longest_word("one", "two", "three") == "three"

# # Write build_sentence(separator, *words) returning one joined string.


# def build_sentence(separator, *words):
#     return separator.join(words)


# assert build_sentence(',', "one", "two", "three") == "one,two,three"


# # Write describe_scores(student_name, *scores) returning name, number of scores and average.
# def describe_scores(student_name, *scores):
#     return student_name, len(scores), average(*scores)


# assert describe_scores("Max", 97, 98, 99) == ("Max", 3, 98)


# # Part C - Positional unpacking

# # Create a list [10, 20, 30] and unpack it into a function expecting three positional parameters.
# def abc(a, b, c):
#     pass


# abc(*[10, 20, 30])

# # Create a tuple containing first_name, last_name, city and call a function using *tuple.
# person = ("Max", "Payne", "New York")


# def func(first_name, last_name, city):
#     print(f"{first_name} {last_name} from {city}")


# func(*person)

# # Use starred assignment: first, *middle, last = values. Test with several list lengths.
# first, *middle, last = [1, 2, 3]
# assert first == 1
# assert middle == [2]
# assert last == 3

# first, *middle, last = [1, 2]
# assert first == 1
# assert middle == []
# assert last == 2

# # Explain in comments the difference between * in a function definition and * in a function call.
# # def func(*args) - packs positional arguments into a tuple
# # func(*[arg1, arg2]) - unpacks an iterable into positional arguments


# # Part D - **kwargs

# # Write show_profile(**info) and iterate over all key/value pairs.
# def show_profile(**info):
#     for key, value in info.items():
#         print(key, value)


# show_profile(name="Max", sex="M")

# # Write create_user(username, **details) returning one dictionary
# # containing username plus all supplied details.


# def create_user(username, **details):
#     user = {"username": username}
#     user.update(details)
#     return user


# print(create_user("user", password="secret"))

# # Write build_product(name, price, **metadata) returning a dictionary.


# def build_product(name, price, **metadata):
#     return {"name": name, "price": price, **metadata}


# print(build_product("t-shirt", 10.00, size="M", color="blue"))

# # Write a function that accepts **settings and returns only settings whose value is not None.


# def non_none_settings(**settings):
#     return {key: value
#             for key, value in settings.items()
#             if value is not None}


# print(non_none_settings(setting1=True, setting2=False, setting3=None))

# # Call a normal named-parameter function using **dictionary unpacking.
# # Ensure dictionary keys match parameter names.


# def print_full_name(first_name, last_name):
#     print(f"{first_name} {last_name}")


# person = {
#     "first_name": "Max",
#     "last_name": "Payne"
# }
# print_full_name(**person)


# # Part E - Combining parameters

# # Create log_event(event_type, *messages, **metadata) returning a structured dictionary.
# def log_event(event_type, *messages, **metadata):
#     return {"event_type": event_type, "messages": list(messages), **metadata}


# print(log_event("info", "system", "update planned", time="00:00"))

# # Create calculate_order(customer, *prices, **options).
# # Support an optional discount and shipping fee in options.


# def calculate_order(customer, *prices, **options):
#     subtotal = 0

#     for price in prices:
#         subtotal += price

#     discount = options.get("discount", 0)
#     shipping = options.get("shipping", 0)

#     total = subtotal - discount + shipping

#     return {
#         "customer": customer,
#         "subtotal": subtotal,
#         "discount": discount,
#         "shipping": shipping,
#         "total": total
#     }


# print(calculate_order("Max Payne", 10.00, 20.00, shipping=5.00))

# # Create a function where explicit named parameters would be clearer than **kwargs.
# # Write both versions and compare readability in comments.


# def create_user(username, age, city):
#     """Explicit username, age and city"""
#     return {
#         "username": username,
#         "age": age,
#         "city": city,
#     }


# def create_user_kwargs(username, **kwargs):
#     """Explicit username and optional keywords"""
#     return {
#         "username": username,
#         **kwargs,
#     }


# print(create_user("user", 18, "NY"))
# print(create_user_kwargs("user", age=18, city="NY"))

# # Create at least three calls to the same flexible function
# # with substantially different numbers of arguments.
# pass


# # Part F - Applied challenge: Report builder

# # Build a flexible report system without files.
# # create_report(title, *sections, **metadata) should return a dictionary.
# # Each section can be a string or a small dictionary; choose and document your design.
# # Metadata may include author, department, version, confidential and date.
# def create_report(title, *sections, **metadata):
#     """ Creates a report.
#     Each section is a string.
#     Possible metadata: author, department, version, confidential and date
#     """
#     return {
#         "title": title,
#         "sections": list(sections),
#         "metadata": metadata,
#     }


# report = create_report(
#     "Monthly Report",
#     "Intro",
#     "Sales Evaluation",
#     "Summary",
#     author="Max",
#     department="Sales",
# )

# # Write summarize_report(report) that returns a readable multi-line string.


# def summarize_report(report):
#     lines = [
#         f"Report: {report["title"]}",
#         "Sections:",
#     ]

#     for section in report["sections"]:
#         lines.append(f"- {section}")

#     lines.append("Metadata:")
#     for key, value in report["metadata"].items():
#         lines.append(f"- {key}: {value}")

#     return "\n".join(lines)


# print(summarize_report(report))

# # Write count_words(*sections) that counts words across all supplied textual sections.


# def count_words(*sections):
#     total_words = 0

#     for section in sections:
#         total_words += len(section.split())

#     return total_words


# print(count_words(*report["sections"]))

# # Use dictionary unpacking to create at least two reports from predefined metadata dictionaries.
# metadata_1 = {
#     "author": "Alice",
#     "department": "Sales"
# }

# metadata_2 = {
#     "author": "Bob",
#     "department": "Engineering"
# }

# report_1 = create_report(
#     "Sales Report",
#     "Introduction",
#     "Sales Results",
#     **metadata_1,
# )

# report_2 = create_report(
#     "Engineering Report",
#     "Overview",
#     "Technical Results",
#     **metadata_2,
# )

# print(summarize_report(report_1))
# print(summarize_report(report_2))

# # Demonstrate at least one case where your function deliberately ignores or handles
# # a missing optional metadata field.
# report_3 = create_report(
#     "No Metadata Report",
#     "Overview",
#     "Results"
# )

# print(summarize_report(report_3))


# Part G - Stretch challenges

# Write merge_settings(defaults, **overrides) returning a new dictionary without modifying defaults.
def merge_settings(defaults, **overrides):
    return {
        **defaults,
        **overrides
    }


defaults = {
    "setting": False
}

print(merge_settings(defaults, setting=True))

# Write call_summary(function_name, *args, **kwargs) returning a string describing what would be called.


def call_summary(function_name, *args, **kwargs):
    return f"{function_name} called with args={args}, kwargs={kwargs}"


print(call_summary("func", 1, kwarg="2"))

# Write a flexible statistics function that returns count, total, average, min and max for *numbers.
# Implement the calculations manually where reasonable.


def statistics(*numbers):
    if not numbers:
        raise ValueError("At least one number is required")

    count = 0
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        count += 1
        total += number

        if number < minimum:
            minimum = number

        if number > maximum:
            maximum = number

    average = total / count

    return {
        "count": count,
        "total": total,
        "average": average,
        "min": minimum,
        "max": maximum,
    }


print(statistics(1, 2, 3))

# Create five “predict the output” scope questions and verify your predictions.
# 1
x = "global"


def show():
    x = "local"
    print(x)  # local


show()
print(x)  # global

# 2
x = "global"


def outer():
    x = "outer"

    def inner():
        print(x)  # outer
    inner()


outer()

# 3


def show():
    print(len("build-in"))  # 'len' has build-in scope


show()

# 4
count = 10


def increase():
    count = 20  # shadowing
    count += 5
    print(count)  # 25


increase()
print(count)  # 10

# 5
value = "global"


def outer():
    value = "outer"

    def inner():
        value = "inner"
        print(value) # inner

    inner()
    print(value) # outer


outer()
print(value) # global
