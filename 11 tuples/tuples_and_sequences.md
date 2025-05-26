# Tuples and Sequences

**Tuples** are similar to lists but with two main differences:

- Tuples are **ordered**, meaning items have a defined order.
- Tuples are **immutable**, so items cannot be changed after creation.

## Creating Tuples

my_tuple = (1, 2, 3)

## Accessing Elements

Like lists, you access by index:

print(my_tuple) # Output: 1

## Benefits of Tuples

- They use less memory than lists.
- Their immutability helps protect data from accidental changes.

## Mixed Data Types

Tuples can contain elements of different types:

mixed = (1, "hello", 3.14)
print(mixed)

## Important

Attempting to modify a tuple, like `my_tuple[1] = 10`, will raise a `TypeError`.

---
