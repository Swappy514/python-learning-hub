# Problem-Solving and Debugging: Loop Control Statements

# Example of a common bug: infinite loop due to missing increment

count = 0
while count < 5:
    print("Count:", count)
    # Missing increment will cause infinite loop if uncommented
    # count += 1

# Correct loop with increment
count = 0
while count < 5:
    print("Count:", count)
    count += 1
