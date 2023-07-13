# collect the necessary inputs: principal, annual rate, years
# calculate the EMI
# Reveal the user 

def main():
    print(" This is a Every Month Installment calculator ")
    print("")


    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the amount interest rate:"))
    years = int(input("Input amount of years: "))
    

    monthly_interest_rate = apr /1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate /(1-(1 + monthly_interest_rate) ** (-amount_of_months))
    print("The monthly payment for this loan is : " + str(monthly_payment))

main()