# Problem-Solving and Debugging: Nested Conditions

Nested conditions often cause logic bugs when indentations or order are mixed up.

**Example:**  
Suppose you want:

- Print "Excellent!" if the score ≥ 75
- Print "Passed!" if 50 ≤ score < 75
- Print "Needs Improvement" if score < 50

score = 85
if score >= 50:
if score >= 75:
print("Excellent!")
else:
print("Passed!")
else:
print("Needs Improvement")
**Output:**
Excellent!

**Tip:**  
Carefully track your `if`, `elif`, and `else` blocks to avoid unreachable code or logic errors.
