# List Methods in Python

numbers = [1, 2, 3]

# Append an element to the list
numbers.append(4)
print("After append:", numbers)  # Output: [1, 2, 3, 4]

# Remove element by value
numbers.remove(2)
print("After remove:", numbers)  # Output: [1, 3, 4]

# Pop the last element
last = numbers.pop()
print("Popped element:", last)   # Output: 4
print("After pop:", numbers)     # Output: [1, 3]

# Sort the list
numbers.sort()
print("Sorted list:", numbers)   # Output: [1, 3]
