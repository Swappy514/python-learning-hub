# Nested Loops Example

# Print a multiplication table (1 to 5)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")  # formatted width 3
    print()  # new line after each row
