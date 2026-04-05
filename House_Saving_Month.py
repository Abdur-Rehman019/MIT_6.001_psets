yearly_salary = float(input("enter yearly salary: "))
portion_saved = float(input("saved salary portion: "))
home_cost = float(input("Cost of Dream Home :"))
semi_annual_raise =float(input("Raise After Every 6 months: "))
initial_deposit = float(input("Enter Initial Deposit: "))


#down payment calculation
portion_down_payment = 0.25 * home_cost
amount_saved = 0
months = 0
rate = 0.05
semi_month = 0

#monthly salary calculation

monthly_salary = yearly_salary/12
monthly_savings = monthly_salary * portion_saved

while(amount_saved < portion_down_payment): # amount saved is 0
            
    return_investment = amount_saved * (rate/12)
    monthly_savings = monthly_salary * portion_saved
    amount_saved = monthly_savings + return_investment + amount_saved
    months = months + 1
    if months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)
    

print(months)