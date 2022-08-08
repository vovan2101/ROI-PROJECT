#1)Income:
#Rental Income = 2000$, Laundry income = 0, Storage = 0, itc = 0
#Total month rental income 2000$

#2) Expenses:
#Tax = 150$, insurance = 100$, utilies: electric, whater, suor, garbage, gas = 0$.
# HOA = $, Snow = $, Vacancy = 100$, reapirs = 100$, capex = 100$, property manegnment = 200$, mortgage = 800$.
#Expenses total = 1600$
#
#3) Cash Flow:
#income(2000$) - Expenses(1600$)
#Total cash flow = 400$

#4) cash on cash ROI
#Down Payment = 40000$, Closing costs = 3000$, Rehab budget = 7000$.
#Total investment = 50000$
#
#400$ * 12 = 4800$
# 50000/4800$ = 9.40%
# cash on cash ROI = 9.40%


class Roi:
    def __init__(self, customer):
        self.customer = customer
        self.inc_dict = {}
        self.exp_dict = {}
        self.cash_flow = {}
        self.cash_on_cash = {}


    def inc(self):
        while True:
            try:
                self.inc_dict["Rental income"] = int(input("\nWhat is your rental income? "))
                self.inc_dict["Laundry income"] = int(input("\nWhat is your laundry income? "))
                self.inc_dict["Storage income"] = int(input("\nWhat is your storage income? "))
                total_income = (sum(self.inc_dict.values()))
                print("\n" + '*' * 26)
                print(f"Your total income is {total_income}$")
                print('*' * 26)

                break
            except:
                print("Invalid input. Please enter a number")

    def exp(self):
        while True:
            try:
                self.exp_dict["tax"] = int(input("\nHow much is your tax? "))
                self.exp_dict["insurance"] = int(input("\nHow much is your insurance? "))
                self.exp_dict["electric"] = int(input("\nHow much you pay for utilities? "))
                self.exp_dict["water"] = int(input("\nHow much you pay for water? "))
                self.exp_dict["garbage"] = int(input("\nHow much you pay for garbage? "))
                self.exp_dict["gas"] = int(input("\nHow much you pay for gas? "))
                self.exp_dict["hoa"] = int(input("\nHow much you pay for HOA? "))
                self.exp_dict["snow"] = int(input("\nHow much you pay for snow cleaning? "))
                self.exp_dict["vacancy"] = int(input("\nHow much you pay for vacancy? "))
                self.exp_dict["repair"] = int(input("\nHow much you pay for repair? "))
                self.exp_dict["capex"] = int(input("\nHow much you pay for capex? "))
                self.exp_dict["property"] = int(input("\nHow much you pay for property? "))
                self.exp_dict["mortgage"] = int(input("\nHow much you pay for mortgage? "))
                total_expenses = (sum(self.exp_dict.values()))
                print("\n" + '*' * 27)
                print(f"Your total expenses = {total_expenses}$")
                print('*' * 27)
                break
            except:
                print("Invalid input. Please enter a number")


    def _cash_flow(self):
        self.cash_flow = (sum(self.inc_dict.values()) - sum(self.exp_dict.values())) * 12
        print("\n" + '*' * 23)
        print(f"Your cash flow = {self.cash_flow}$")
        print('*' * 23)


    def _cash_on_cash(self):
        while True:
            try:
                self.cash_on_cash["Down Payment"] = int(input("\nWhat is your down payment? "))
                self.cash_on_cash["Closing costs"] = int(input("\nWhat is your closing costs? "))
                self.cash_on_cash["Rehab budget"] = int(input("\nWhat is your rehab budget? "))
                total_cash_on_cash = (sum(self.cash_on_cash.values()))
                print("\n" + '*' * 26)
                print(f"yours investments = {total_cash_on_cash}$")
                print('*' * 26)
                break
            except:
                print("Invalid input. Please enter a number")

    def roi(self):
            total_rio = sum(self.cash_on_cash.values()) / self.cash_flow
            print("\n" + '*' * 30)
            print(f"Your RIO = {total_rio}%")
            print('*' * 30)


def ask():
    ask_again = input("\nIs it anything else I can do for you?\nagain/change/quit: ").lower()
    if ask_again == "quit":
        print("\nTHANKS FOR YOUR BUSINESS!!!")
        return False
    elif ask_again == "change":
        change = input("What would you like to change? income/expenses/investments? ").lower()
        if change == "income":
            calc.inc()
            calc._cash_flow()
            calc.roi()
            ask()
        elif change == "expenses":
            calc.exp()
            calc._cash_flow()
            calc.roi()
            ask()
        elif change == "investments":
            calc._cash_on_cash()
            calc.roi()
            ask()
        else:
            print("Invalid input. Please try again")
    elif ask_again == "again":
        calc.inc()
        calc.exp()
        calc._cash_flow()
        calc._cash_on_cash()
        calc.roi()
        ask()
    else:
        input("Invalid input. Please try again: ")



customer = "VLAD"
calc = Roi(customer)
print('\n' + '*'*81)
print(f"HEY {calc.customer}, WELCOME TO THE BIGGER POCKETS COMPANY! LET'S FIND A GRETE DEAL FOR YOU!")
print('*' * 81)
calc.inc()
calc.exp()
calc._cash_flow()
calc._cash_on_cash()
calc.roi()
ask()
