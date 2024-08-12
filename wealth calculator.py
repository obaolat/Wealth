import sys

def wealth_per_year(curr, rate, monthly_savings, years):
    for year in range(1, years+1):
        interest = curr * (rate/100)
        curr += interest + (monthly_savings * 12)
        print(f"Year {year}: Total wealth ={curr:.2f} ")
        
def freedom_wealth(curr, rate, monthly_savings, target):
    final_freedom = 0
    while True:
        final_freedom += 1
        interest = curr * (rate/100)
        curr += interest + (monthly_savings * 12)
        if curr > target:
            print (f"You will financial freedom in {final_freedom} years! Keep grinding!! ")
            
        
        
def calculator():
    run = input("Which would you like to calculate? Type in 'returns' or 'freedom' ")
    try:
        curr = float(input("How much do you have right now: "))
        rate = float(input("How much is your estimated rate of return (%): "))
        monthly_savings = float(input("How much can you save per month:  "))
    except ValueError:
        print("You can only input numbers")
        sys.exit()
    if run == 'returns':
        years = int(input("How many years are you investing for: "))
        wealth_per_year(curr, rate, monthly_savings, years)
    elif run == 'freedom':
        try:
            target = float(input("How much money do you need to be financially free?"))
        except ValueError:
            print("You can only input numbers")
            sys.exit()
        freedom_wealth(curr, rate, monthly_savings, target)
    else:
        print("You have not typed your options correctly, you can only typem 'returns' or freedom \n Tip: Check the spelling  ")
        
        

calculator()