customer_name = input("Welcome, what is your name? ")
starting_balance = 5000.25
print(f"Hello {customer_name}, your starting balance is {starting_balance} ")
pay_check = float(input("How much of your paycheck would you like to deposit? "))
expenditure_item = input("Seems as if you went shopping, what'd ya buy?? ")
expenditure = input(f"How much does {expenditure_item} cost? ")

ending_balance = int(starting_balance + pay_check)
ending_balance = ending_balance - int(expenditure)

def checking_balance(user_names, balances, deposits, expense_items, expense_amounts, ending_balance):
    customer_name = user_names
    starting_balance = balances
    pay_check = deposits
    expenditure_items = expense_items
    expenditure = expense_amounts
    ending_balance = balances+deposits-int(expense_amounts)
    print(f"Ok, so after spending {expense_amounts} on {expense_items}, your current checking balance is: {ending_balance}")

checking_balance(customer_name, starting_balance, pay_check, expenditure_item, expenditure, ending_balance)