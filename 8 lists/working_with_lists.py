# Working with Lists: Common operations

numbers = [1, 2, 3, 4, 5]

# Append an item
numbers.append(6)
print("After append:", numbers)

# Insert an item at position 2
numbers.insert(2, 10)
print("After insert:", numbers)

# Remove item by value
numbers.remove(3)
print("After remove:", numbers)

# Pop last item
last_item = numbers.pop()
print("Popped item:", last_item)
print("After pop:", numbers)

# Length of the list
print("List length:", len(numbers))
