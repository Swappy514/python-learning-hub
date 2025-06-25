# Problem-Solving and Debugging: Nested Conditions

# Example 1: Detect logic error in nested conditions
score = 45
passing_grade = 50

if score >= passing_grade:
    if score >= 75:
        print("Excellent!")
    else:
        print("Passed!")
else:
    print("Needs Improvement")  # Correct: Will print for score < 50
