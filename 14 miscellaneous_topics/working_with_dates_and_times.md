# Working with Dates and Times

Python's `datetime` module allows manipulation of date and time objects.

### Examples:

- Get current date/time:

now = datetime.datetime.now()
print(now)

- Create a specific date:

birth_date = datetime.date(1990, 5, 17)
print(birth_date)

- Calculate time difference:

delta = now.date() - birth_date
print(delta.days) # Number of days

- Format dates to strings with `strftime`:

print(now.strftime("%B %d, %Y")) # e.g. "July 27, 2025"

These functions are essential for scheduling, logging, and timestamps.
