# For Loop in Detail

A `for` loop runs through items of any sequence like lists, tuples, or strings.

### Example 1: Loop over list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print("Fruit:", fruit)

**Output:**

Fruit: apple
Fruit: banana
Fruit: cherry

### Example 2: Loop with index

To get both index and item:

for index in range(len(fruits)):
print(f"Index {index}: {fruits[index]}")

**Output:**

Index 0: apple
Index 1: banana
Index 2: cherry

Loops make processing collections or performing repeated actions straightforward.
