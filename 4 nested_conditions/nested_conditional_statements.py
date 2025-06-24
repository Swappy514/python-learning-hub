# Nested Conditional Statements Example

# Determine eligibility for an event

age = 17
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Entry allowed.")
    else:
        print("Ticket required.")
else:
    if has_ticket:
        print("Too young, even with ticket.")
    else:
        print("Too young and no ticket.")

# Try with age = 20 and has_ticket = False for other branches
