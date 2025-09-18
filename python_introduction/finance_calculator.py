# Get user input for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses
# Assume a simple annual interest rate of 5%
interest_rate = 0.05
# Calculate the projected annual savings
# Formula: (Monthly Savings * 12) + (Monthly Savings * 12 * 0.05)
projected_savings_one_year = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)
# Display the results
print(f"Your monthly savings: ${monthly_savings:,.2f}")
print(f"Your projected annual savings with 5% interest: ${projected_savings_one_year:,.2f}")