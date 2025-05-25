# Set Operations in Python

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: items in either set
union_set = set_a.union(set_b)
print("Union:", union_set)  # Output: {1,2,3,4,5,6}

# Intersection: items in both sets
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)  # Output: {3,4}

# Difference: items in set_a but not in set_b
diff_set = set_a.difference(set_b)
print("Difference (A-B):", diff_set)  # Output: {1,2}

# Symmetric Difference: items in either set, but not both
sym_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", sym_diff_set)  # Output: {1,2,5,6}
