# my_tool.py
# Author: Fouzan Haider


class AppointmentLookup:
    """A tool that stores available appointment times."""

    def __init__(self, appointments):
        # Store the appointment schedule.
        self.appointments = appointments

    def find_day(self, text):
        """Find a weekday mentioned in the customer's message."""

        # Convert the message to lowercase for matching.
        text = text.lower()

        # Check each day in the appointment schedule.
        for day in self.appointments:
            # Return the day if it appears in the message.
            if day.lower() in text:
                return day

        # Return None when no known day is found.
        return None

    def available_times(self, day):
        """Return available appointment times for a given day."""

        # Check whether the requested day exists.
        if day in self.appointments:
            return self.appointments[day]

        # Return None when the day is not available.
        return None
