# Industry Example: Employee Pay Calculation with Overtime

This function calculates an employee’s pay:

- Regular hourly rate applies up to 40 hours.
- Overtime hours (>40) paid at 1.5 times the regular rate.

## Code:

def calculate_pay(hours_worked, hourly_rate=20):
if hours_worked <= 40:
return hours_worked _ hourly_rate
else:
regular_pay = 40 _ hourly_rate
overtime_hours = hours_worked - 40
overtime_pay = overtime_hours _ hourly_rate _ 1.5
return regular_pay + overtime_pay

pay = calculate_pay(45)
print(f"Total pay for 45 hours: ${pay:.2f}")

## Sample output:

Total pay for 45 hours: $950.00

This example covers default arguments, conditionals, and return values commonly seen in payroll systems.
