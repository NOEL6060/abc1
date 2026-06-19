def calculate_emi(principal, annual_rate, years):

```
monthly_rate = annual_rate / 12 / 100
months = years * 12

emi = (
    principal * monthly_rate *
    (1 + monthly_rate) ** months
) / (
    ((1 + monthly_rate) ** months) - 1
)

return round(emi, 2)
```

loan_amount = float(input("Enter loan amount: "))
interest_rate = float(input("Enter annual interest rate (%): "))
loan_years = int(input("Enter loan tenure (years): "))

emi = calculate_emi(
loan_amount,
interest_rate,
loan_years
)

print(f"Monthly EMI: ₹{emi}")

