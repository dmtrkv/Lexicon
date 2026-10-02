"""The booking system demo app."""

from datetime import date, datetime, time, timedelta

from .domain import BookableItem, Customer
from .service import BookingService


def create_demo_system():
    """Create a booking system with sample customers and bookable items."""
    system = BookingService()
    system.register_customer(Customer("customer-1", "Ann"))
    system.register_customer(Customer("customer-2", "Bob"))
    system.register_bookable_item(
        BookableItem("room-1", "Meeting Room", "meeting", 25)
    )
    system.register_bookable_item(
        BookableItem("room-2", "Relax Room", "relax", 40)
    )
    system.register_bookable_item(
        BookableItem("bike-1", "City Bike", "bike", 10)
    )
    return system


def _read_period():
    """Read and validate a start and end from the command line."""
    today = date.today()
    default_start = datetime.combine(today, time(12, 00))
    default_end = datetime.combine(today + timedelta(days=1), time(11, 59))
    print("\n📅 Enter the booking period")
    start_text = input("  Start  [{}]: ".format(
        default_start.strftime("%Y-%m-%d")
    )).strip()
    end_text = input("  End    [{}]: ".format(
        default_end.strftime("%Y-%m-%d")
    )).strip()
    try:
        start = datetime.fromisoformat(
            start_text) if start_text else default_start
        end = datetime.fromisoformat(end_text) if end_text else default_end
    except ValueError:
        raise ValueError("enter dates as YYYY-MM-DD [HH:MM]")
    BookingService.validate_period(start, end)
    return start, end


def _show_items(items, marker="•"):
    """Print item IDs, names, and categories, or an empty-list message."""
    if not items:
        print("  └─ None")
        return
    for item in items:
        print("  {} {}  [{}]".format(marker, item.name, item.id))


def _show_customers(system):
    print("\n👤 CUSTOMERS")
    for customer in system.get_customers():
        print("  • {}  [{}]".format(customer.name, customer.id))


def _choose_from_list(entries, label, description):
    """Display numbered choices and return the selected entry."""
    if not entries:
        raise ValueError("no {} are registered".format(label.lower()))

    print("\n{}".format(label.upper()))
    for number, entry in enumerate(entries, 1):
        print("  {}. {}  [{}]".format(number, description(entry), entry.id))

    choice_text = input(
        "Choose a number (1-{}): ".format(len(entries))).strip()
    try:
        choice = int(choice_text)
    except ValueError:
        raise ValueError("enter a number from 1 to {}".format(len(entries)))
    if choice < 1 or choice > len(entries):
        raise ValueError("choose a number from 1 to {}".format(len(entries)))
    return entries[choice - 1]


def _choose_customer(system):
    return _choose_from_list(
        system.get_customers(), "Customers", lambda customer: customer.name
    )


def _choose_bookable_item(system):
    return _choose_from_list(
        system.get_bookable_items(),
        "Bookable items",
        lambda item: "{} ({})".format(item.name, item.category),
    )


def _show_bookable_items(system):
    print("\n🏷️  BOOKABLE ITEMS")
    _show_items(system.get_bookable_items())


def _choose_active_booking(system, action):
    """Choose an active booking, or return None to go back to the menu."""
    bookings = system.search_bookings(status="active")
    if not bookings:
        print("\nNo active bookings to {}.".format(action))
        return None

    print("\nActive bookings:")
    for number, booking in enumerate(bookings, 1):
        start = booking.start.strftime("%Y-%m-%d")
        end = booking.end.strftime("%Y-%m-%d")
        print("  {}. {} for {} ({} to {})".format(
            number, booking.item.name, booking.customer.name,
            start, end
        ))

    choice_text = input(
        "Choose a booking number, or press Enter to go back: "
    ).strip()
    if not choice_text:
        return None
    try:
        choice = int(choice_text)
    except ValueError:
        raise ValueError("enter a number from 1 to {}".format(len(bookings)))
    if choice < 1 or choice > len(bookings):
        raise ValueError("choose a number from 1 to {}".format(len(bookings)))
    return bookings[choice - 1]


def _read_menu_choice():
    print("\n")
    print("🏨 BOOKING SYSTEM         ")
    # print("")
    print("  1  📊  Period summary   ")
    print("  2  🔎  Check one item   ")
    print("  3  ➕  Create a booking ")
    print("  4  🔄  Change a booking ")
    print("  5  ❌  Cancel a booking ")
    print("  6  👋  Exit                       ")
    # print("└────────────────────────────────────┘")
    return input("➡️  Choose an option (1-6): ").strip()


def _pause_before_menu():
    """Wait for a key press before displaying the menu again."""
    try:
        import msvcrt
    except ImportError:
        input("\nPress Enter to continue...")
    else:
        print("\nPress any key to continue...", end="", flush=True)
        msvcrt.getch()
        print()


def run_menu(system=None):
    """Run the interactive menu using a supplied or example booking system."""
    if system is None:
        system = create_demo_system()

    print("\n✨ WELCOME TO THE BOOKING SYSTEM!")
    _show_customers(system)
    _show_bookable_items(system)

    while True:
        try:
            choice = _read_menu_choice()
            if choice == "1":
                start, end = _read_period()
                available, booked = system.summarize_items(start, end)
                print("\n📊 AVAILABILITY SUMMARY")
                print("  Period: {} → {}".format(
                    start.strftime("%Y-%m-%d"),
                    end.strftime("%Y-%m-%d"),
                ))
                print("\n🟢 AVAILABLE ({})".format(len(available)))
                _show_items(available, "🟢")
                print("\n🔴 BOOKED ({})".format(len(booked)))
                _show_items(booked, "🔴")
            elif choice == "2":
                item = _choose_bookable_item(system)
                start, end = _read_period()
                if system.is_available(item, start, end):
                    print(
                        "\n✅ AVAILABLE: {} is free for that period.".format(item.name))
                else:
                    print(
                        "\n⛔ UNAVAILABLE: {} is booked for that period.".format(item.name))
            elif choice == "3":
                customer = _choose_customer(system)
                item = _choose_bookable_item(system)
                start, end = _read_period()
                booking = system.create_booking(customer, item, start, end)
                print("\n✅ BOOKING CREATED\n  ID: {}\n  Item: {}\n  Customer: {}".format(
                    booking.id, item.name, customer.name
                ))
            elif choice == "4":
                booking = _choose_active_booking(system, "change")
                if booking is None:
                    continue
                else:
                    start, end = _read_period()
                    booking = system.change_booking_period(
                        booking.id, start, end)
                    print("\n✅ BOOKING UPDATED\n  ID: {}\n  New period: {} → {}".format(
                        booking.id,
                        booking.start.strftime("%Y-%m-%d"),
                        booking.end.strftime("%Y-%m-%d"),
                    ))
            elif choice == "5":
                booking = _choose_active_booking(system, "cancel")
                if booking is None:
                    continue
                else:
                    booking = system.cancel_booking(booking.id)
                    print("\n✅ BOOKING CANCELLED\n  ID: {}".format(booking.id))
            elif choice == "6":
                print("\n✨ GOODBYE!\n")
                return
            else:
                print("\nINVALID CHOICE\n  Choose a number from 1 to 6.")
        except (ValueError, TypeError) as error:
            print("\nOPERATION NOT COMPLETED\n  Reason: {}".format(error))

        _pause_before_menu()
