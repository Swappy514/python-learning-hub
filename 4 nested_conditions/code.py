# Industry Example: Loan Eligibility Check using Nested Conditions

credit_score = 720
income = 50000
loan_amount = 200000

if credit_score >= 700:
    if income >= 40000:
        if loan_amount <= 5 * income:
            print("Loan Approved")
        else:
            print("Loan amount too high for your income.")
    else:
        print("Income too low.")
else:
    print("Credit score too low.")
