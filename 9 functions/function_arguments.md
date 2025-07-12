# Function Arguments

Functions can accept various types of arguments:

- **Positional arguments:** passed in order.
- **Default arguments:** have default values if not provided:
  def func(arg=default_value):
  ...
- **Keyword arguments:** passed by name, allowing order flexibility.

## Examples:

def describe_person(name, age):
print(f"{name} is {age} years old.")

def describe_pet(name, animal="dog"):
print(f"{name} is a {animal}.")

describe_pet("Buddy") # Uses default 'dog'
describe_pet("Mittens", "cat")

def info(city, country):
print(f"City: {city}, Country: {country}")

info(country="USA", city="New York")

Using these forms allows flexible and readable function calls.
