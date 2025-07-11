# Industry Example: Calculate Employee Pay with Overtime

def calculate_pay(hours_worked, hourly_rate=20):
    """Calculate total pay with overtime (1.5x) for hours above 40."""
    if hours_worked <= 40:
        return hours_worked * hourly_rate
    else:
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        return regular_pay + overtime_pay

pay = calculate_pay(45)
print(f"Total pay for 45 hours: ${pay:.2f}")
