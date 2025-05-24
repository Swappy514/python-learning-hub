# Sets in Python
# Sets are unordered collections of unique items

# Example 1: Creating a set
my_set = {1, 2, 3, 2, 1}
print("Set (duplicates removed):", my_set)

# Example 2: Adding and removing elements
my_set.add(4)
print("After adding 4:", my_set)

my_set.remove(2)
print("After removing 2:", my_set)

# Example 3: Checking membership
print("Is 3 in set?", 3 in my_set)