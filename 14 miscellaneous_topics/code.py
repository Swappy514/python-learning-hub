# Industry Example: Simple Log with Timestamp and Error Handling

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
