# Industry Example: Logging with Timestamp and Exception Handling

This example demonstrates:

- Getting and formatting current timestamps.
- Logging events with time info.
- Handling user input and common exceptions safely.

### Code:

import datetime

def log_event(event):
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{time_stamp} - {event}")

try:
num = int(input("Enter a divisor: "))
result = 100 / num
log_event(f"Division successful: 100 / {num} = {result}")
except ValueError:
log_event("Invalid input for divisor.")
except ZeroDivisionError:
log_event("Attempted division by zero.")
except Exception as e:
log_event(f"Unexpected error: {e}")
finally:
log_event("Process ended.")

### Sample output:

2025-07-27 17:00:00 - Division successful: 100 / 4 = 25.0
2025-07-27 17:00:00 - Process ended.

or, in case of error:

2025-07-27 17:05:00 - Invalid input for divisor.
2025-07-27 17:05:00 - Process ended.

This pattern is common in real-world logging and error tracking systems.
