Sequence of Instructions
A Python program’s execution flows line by line, top to bottom, unless you use special statements for loops, functions, or conditions.
Each statement completes before the next begins (this is called sequential execution).

Example 1: Sequential Steps
Code
x = 5
y = 10
total = x + y
print("Total:", total)
Output:
Total: 15

Each statement uses variables from previous ones.

Example 2: Updating Variables in Sequence
Code
counter = 0
counter = counter + 1
counter = counter + 5
print("Counter:", counter)
Output:
Counter: 6
Each line changes the value for use in later lines.

Key point:
Code runs in the order it’s written, unless directed otherwise by functions, loops, or conditions.
