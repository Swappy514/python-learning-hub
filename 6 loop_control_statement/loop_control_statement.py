# Loop Control Statements: break, continue, pass

for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue  # Skip the rest of this iteration
    if i == 5:
        print("Breaking at 5")
        break  # Exit the loop entirely
    print("Number:", i)
else:
    # This else runs only if no break occurs
    print("Completed loop without break")

# pass example (placeholder)
for i in range(3):
    pass  # Placeholder, no action
