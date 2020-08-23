import math

action = input("""What do you want to calculate?
type "n" for the number of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:""")

if action == "n":
    pri = int(input("Enter the credit principal"))
    monthly_payment = int(input("Enter the monthly payment:"))
    interest = float(input("Enter the credit interest:"))
    i = (interest * 0.01) / 12
    number_periods = math.ceil(math.log(monthly_payment / (monthly_payment - i * pri), 1 + i))
    years = int(number_periods // 12)
    months = math.ceil(int(number_periods % 12))
    print(number_periods)
    if number_periods < 13:
        print("You need ", months, " months to repay this credit!")
    elif number_periods % 12 == 0:
        print("You need ", years, " years to repay this credit!")
    elif years == 1:
        if number_periods % 12 == 0:
            print("You need ", years, " year to repay this credit!")
        else:
            print("You need ", years, "year and ", months, " months to repay this credit!")
    else:
        print("You need ", years, "years and ", months, " months to repay this credit!")

elif action == "a":
    pri = int(input("Enter the credit principal"))
    number_periods = int(input("Enter the number of periods:"))
    interest = float(input("Enter the credit interest:"))
    i = (interest * 0.01) / 12
    annuity = pri * ((i * math.pow(1 + i, number_periods)) / (math.pow(1 + i, number_periods) - 1))
    print("Your annuity payment =", math.ceil(annuity), "!")

elif action == "p":
    annuity = float(input("Enter the annuity payment"))
    number_periods = int(input("Enter the number of periods:"))
    interest = float(input("Enter the credit interest:"))
    i = (interest * 0.01) / 12
    pri = annuity / ((i * math.pow(1 + i, number_periods)) / (math.pow(1 + i, number_periods) - 1))
    print("Your credit principal =", pri, "!")

else:
    print("Order not recognised")
