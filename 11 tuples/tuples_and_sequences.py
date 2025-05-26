# Tuples and Sequences in Python

# A tuple is an ordered, immutable collection of items

# Example 1: Creating a tuple
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# Example 2: Accessing tuple elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Example 3: Tuples are immutable (following line would raise error if uncommented)
# my_tuple[1] = 10  # TypeError: 'tuple' object does not support item assignment

# Example 4: Tuples can hold mixed data types
mixed = (1, "hello", 3.14)
print("Mixed tuple:", mixed)
