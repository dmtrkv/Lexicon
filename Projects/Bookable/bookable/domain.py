"""Booking domain objects"""

from datetime import datetime


BOOKING_STATUSES = ("active", "cancelled")


def require(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("{} must be a non-empty string".format(field_name))


class Customer:
    """A person or organization that can make a booking."""

    def __init__(self, customer_id, name):
        require(customer_id, "customer_id")
        require(name, "name")

        self.id = customer_id
        self.name = name


class BookableItem:
    """A resource or service that can be booked."""

    def __init__(self, item_id, name, category, price):
        require(item_id, "item_id")
        require(name, "name")
        require(category, "category")

        if not isinstance(price, (int, float)):
            raise ValueError("price must be a number")
        if price < 0:
            raise ValueError("price must be a non-negative")

        self.id = item_id
        self.name = name
        self.category = category
        self.price = price


class Booking:
    """A customer's reservation of one bookable item for a time period."""

    def __init__(self, booking_id, customer, item, start, end):
        require(booking_id, "booking_id")

        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer")
        if not isinstance(item, BookableItem):
            raise ValueError("item must be a BookableItem")
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("start and end must be datetime values")
        if end <= start:
            raise ValueError("end must be later than start")

        self.id = booking_id
        self.customer = customer
        self.item = item
        self.start = start
        self.end = end
        self.status = BOOKING_STATUSES[0]  # active by default
