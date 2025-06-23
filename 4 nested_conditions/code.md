# Industry Example: Loan Eligibility Check

Financial products often require multiple criteria to be met.  
This scenario uses nested conditions to determine if a customer qualifies for a loan.

**Logic:**

- If credit score ≥ 700:
  - If income ≥ 40,000:
    - If loan ≤ 5× income: **"Loan Approved"**
    - Else: **"Loan amount too high for your income."**
  - Else: **"Income too low."**
- Else: **"Credit score too low."**

**Example:**
credit_score = 720
income = 50000
loan_amount = 200000

if credit_score >= 700:
if income >= 40000:
if loan_amount <= 5 \* income:
print("Loan Approved")
else:
print("Loan amount too high for your income.")
else:
print("Income too low.")
else:
print("Credit score too low.")

**Output (with above values):**
Loan Approved
