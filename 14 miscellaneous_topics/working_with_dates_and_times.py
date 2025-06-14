# Working with Dates & Times

import datetime

# Get current date and time
now = datetime.datetime.now()
print("Now:", now)

# Create a specific date
birth_date = datetime.date(1990, 5, 17)
print("Birth date:", birth_date)

# Time difference between two dates
delta = now.date() - birth_date
print("Days since birth:", delta.days)

# Format date as string
print("Formatted date:", now.strftime("%B %d, %Y"))
