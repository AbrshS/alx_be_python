# finance_calculator.py

# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print("Your monthly savings are:", monthly_savings)
print("Your projected annual savings (with 5% interest) are:", annual_savings)