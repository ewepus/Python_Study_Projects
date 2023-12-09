import sys

while True:
    balance = 0
    destination = str(input()).lower()
    if destination == "end":
        break
    destination = destination.title()
    minimalBudget = str(input().lower())
    if minimalBudget == "end":
        break
    minimalBudgetNumber = int(minimalBudget)
    if minimalBudgetNumber < 0:
        print("invalid")
        break

    while balance < minimalBudgetNumber:
        income = str(input())
        if income == "end":
            sys.exit()
        balance += int(income)

    if (balance - minimalBudgetNumber) >= 0:
        print("Going to %s!" % destination)
