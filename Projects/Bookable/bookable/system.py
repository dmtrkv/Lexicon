"""In-memory ownership and lookup for booking domain objects."""

from datetime import datetime

from .domain import BookableItem, Booking, Customer


class BookingSystem:
    """Store customers, bookable items, and bookings."""

    def __init__(self):
        self._customers = {}
        self._bookable_items = {}
        self._bookings = {}

    def register_customer(self, customer):
        """Register a customer, rejecting an ID that is already in use."""
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer")
        if customer.id in self._customers:
            raise ValueError(
                "customer ID is already registered: {}".format(customer.id))
        self._customers[customer.id] = customer

    def get_customer(self, customer_id):
        """Return a registered customer, or None if the ID is unknown."""
        return self._customers.get(customer_id)

    def register_bookable_item(self, item):
        """Register a bookable item, rejecting an ID that is already in use."""
        if not isinstance(item, BookableItem):
            raise TypeError("item must be a BookableItem")
        if item.id in self._bookable_items:
            raise ValueError(
                "bookable item ID is already registered: {}".format(item.id))
        self._bookable_items[item.id] = item

    def get_bookable_item(self, item_id):
        """Return a registered bookable item, or None if the ID is unknown."""
        return self._bookable_items.get(item_id)

    def register_booking(self, booking):
        """Register a booking, rejecting an ID that is already in use."""
        if not isinstance(booking, Booking):
            raise TypeError("booking must be a Booking")
        if booking.id in self._bookings:
            raise ValueError(
                "booking ID is already registered: {}".format(booking.id))
        self._bookings[booking.id] = booking

    def get_booking(self, booking_id):
        """Return a registered booking, or None if the ID is unknown."""
        return self._bookings.get(booking_id)

    @staticmethod
    def validate_period(start, end):
        """Reject invalid or incomparable start/end datetime values."""
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("start and end must be datetime values")
        try:
            valid_order = end > start
        except (TypeError, ValueError):
            raise ValueError("start and end must use comparable datetimes")
        if not valid_order:
            raise ValueError("end must be later than start")

    def is_available(self, item, start, end):
        """Return whether a registered item has no active booking overlap.

        Periods are half-open: a booking ending at ``start`` or starting at
        ``end`` does not conflict.
        """
        self.validate_period(start, end)
        if not isinstance(item, BookableItem):
            raise TypeError("item must be a BookableItem")
        if self._bookable_items.get(item.id) is not item:
            raise ValueError(
                "bookable item is not registered: {}".format(item.id))

        for booking in self._bookings.values():
            if booking.item.id == item.id and booking.status == "active":
                try:
                    overlaps = booking.start < end and start < booking.end
                except (TypeError, ValueError):
                    raise ValueError(
                        "requested and booked datetimes must be comparable"
                    )
                if overlaps:
                    return False
        return True

    def get_available_items(self, start, end):
        """Return registered items available for the requested period."""
        self.validate_period(start, end)
        return [
            item for item in self._bookable_items.values()
            if self.is_available(item, start, end)
        ]
