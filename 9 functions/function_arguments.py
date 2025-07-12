# Function Arguments: Positional, Default, and Keyword Arguments

# Example 1: Positional arguments
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person("Bob", 30)

# Example 2: Default argument
def describe_pet(name, animal="dog"):
    print(f"{name} is a {animal}.")

describe_pet("Buddy")
describe_pet("Mittens", "cat")

# Example 3: Keyword arguments
def info(city, country):
    print(f"City: {city}, Country: {country}")

info(country="USA", city="New York")
