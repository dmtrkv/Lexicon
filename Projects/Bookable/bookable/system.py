"""In-memory ownership and lookup for booking domain objects."""

from .domain import BookableItem, Booking, Customer


class BookingSystem:
    """Store customers, bookable items, and bookings."""

    def __init__(self):
        self.customers = {}
        self.bookable_items = {}
        self.bookings = {}

    def register_customer(self, customer):
        """Register a customer, rejecting an ID that is already in use."""
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer")
        if customer.id in self.customers:
            raise ValueError(
                "customer ID is already registered: {}".format(customer.id))
        self.customers[customer.id] = customer

    def get_customer(self, customer_id):
        """Return a registered customer, or None if the ID is unknown."""
        return self.customers.get(customer_id)

    def register_bookable_item(self, item):
        """Register a bookable item, rejecting an ID that is already in use."""
        if not isinstance(item, BookableItem):
            raise TypeError("item must be a BookableItem")
        if item.id in self.bookable_items:
            raise ValueError(
                "bookable item ID is already registered: {}".format(item.id))
        self.bookable_items[item.id] = item

    def get_bookable_item(self, item_id):
        """Return a registered bookable item, or None if the ID is unknown."""
        return self.bookable_items.get(item_id)

    def register_booking(self, booking):
        """Register a booking, rejecting an ID that is already in use."""
        if not isinstance(booking, Booking):
            raise TypeError("booking must be a Booking")
        if booking.id in self.bookings:
            raise ValueError(
                "booking ID is already registered: {}".format(booking.id))
        self.bookings[booking.id] = booking

    def get_booking(self, booking_id):
        """Return a registered booking, or None if the ID is unknown."""
        return self.bookings.get(booking_id)
