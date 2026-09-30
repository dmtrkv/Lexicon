"""Booking lifecycle operations."""

from datetime import datetime

from .domain import BookableItem, Booking, Customer


class BookingSystem:
    """Store customers, bookable items, and bookings."""

    def __init__(self):
        self._customers = {}
        self._bookable_items = {}
        self._bookings = {}
        self._next_booking_number = 1

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

    def create_booking(self, customer, item, start, end):
        """Create and register a booking for a registered customer and item."""
        self.validate_period(start, end)
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer")
        if self._customers.get(customer.id) is not customer:
            raise ValueError(
                "customer is not registered: {}".format(customer.id))
        if not isinstance(item, BookableItem):
            raise TypeError("item must be a BookableItem")
        if self._bookable_items.get(item.id) is not item:
            raise ValueError(
                "bookable item is not registered: {}".format(item.id))
        if not self.is_available(item, start, end):
            raise ValueError(
                "bookable item is not available for requested period")

        booking_number = self._next_booking_number
        booking_id = "booking-{}".format(booking_number)
        while booking_id in self._bookings:
            booking_number += 1
            booking_id = "booking-{}".format(booking_number)

        booking = Booking(booking_id, customer, item, start, end)
        self._bookings[booking.id] = booking
        self._next_booking_number = booking_number + 1
        return booking

    def cancel_booking(self, booking_id):
        """Cancel a registered active booking and return it."""
        booking = self.get_registered_booking(booking_id)
        if booking.status != "active":
            if booking.status == "cancelled":
                raise ValueError(
                    "booking is already cancelled: {}".format(booking.id))
            raise ValueError("booking is not active: {}".format(booking.id))

        booking.status = "cancelled"
        return booking

    def change_booking_period(self, booking_id, start, end):
        """Change an active booking's period after checking availability."""
        booking = self.get_registered_booking(booking_id)
        if booking.status != "active":
            if booking.status == "cancelled":
                raise ValueError(
                    "cancelled booking cannot be changed: {}".format(
                        booking.id)
                )
            raise ValueError("booking is not active: {}".format(booking.id))
        self.validate_period(start, end)
        if not self._is_available(booking.item, start, end, booking):
            raise ValueError(
                "bookable item is not available for requested period")

        booking.start = start
        booking.end = end
        return booking

    def get_registered_booking(self, booking_id):
        """Return a registered booking or raise a clear validation error."""
        if not isinstance(booking_id, str):
            raise TypeError("booking_id must be a string")
        if not booking_id.strip():
            raise ValueError("booking_id must be a non-empty string")
        booking = self._bookings.get(booking_id)
        if booking is None:
            raise ValueError(
                "booking is not registered: {}".format(booking_id))
        return booking

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
        return self._is_available(item, start, end)

    def _is_available(self, item, start, end, ignored_booking=None):
        """Check availability, optionally ignoring one booking being changed."""
        self.validate_period(start, end)
        if not isinstance(item, BookableItem):
            raise TypeError("item must be a BookableItem")
        if self._bookable_items.get(item.id) is not item:
            raise ValueError(
                "bookable item is not registered: {}".format(item.id))

        for booking in self._bookings.values():
            if booking is ignored_booking:
                continue
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

    def calculate_booking_cost(self, booking_id):
        """Return a booking's cost using complete elapsed hours and hourly price.

        Partial hours are excluded. The result is the numeric product of
        complete elapsed hours and the item's current price.
        """
        booking = self.get_registered_booking(booking_id)
        duration = booking.end - booking.start
        whole_hours = duration.days * 24 + duration.seconds // 3600
        return whole_hours * booking.item.price

    def search_bookings(self, customer_id=None, item_id=None, status=None):
        """Return bookings matching any supplied filters, in registration order."""
        if customer_id is not None:
            if not isinstance(customer_id, str):
                raise TypeError("customer_id must be a string")
            if not customer_id.strip():
                raise ValueError("customer_id must be a non-empty string")

        if item_id is not None:
            if not isinstance(item_id, str):
                raise TypeError("item_id must be a string")
            if not item_id.strip():
                raise ValueError("item_id must be a non-empty string")

        if status is not None:
            if not isinstance(status, str):
                raise TypeError("status must be a string")
            if status not in ("active", "cancelled"):
                raise ValueError("status must be 'active' or 'cancelled'")

        return [
            booking for booking in self._bookings.values()
            if (customer_id is None or booking.customer.id == customer_id)
            and (item_id is None or booking.item.id == item_id)
            and (status is None or booking.status == status)
        ]