budget = int(input())
season = str(input().lower())
peopleCount = int(input())

if (budget >= 1) and (budget <= 8000):
    if (peopleCount >= 4) and (peopleCount <= 18):
        if season == "spring":
            if (peopleCount >= 4) and (peopleCount <= 6):
                if peopleCount % 2 == 0:
                    remainder = (budget - 3000 * 0.85)
                else:
                    remainder = (budget - 3000 * 0.90)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif (peopleCount >= 7) and (peopleCount <= 11):
                if peopleCount % 2 == 0:
                    remainder = (budget - 3000 * 0.80)
                else:
                    remainder = (budget - 3000 * 0.85)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif peopleCount >= 12:
                if peopleCount % 2 == 0:
                    remainder = (budget - 3000 * 0.70)
                else:
                    remainder = (budget - 3000 * 0.75)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)

        elif season == "summer":
            if (peopleCount >= 4) and (peopleCount <= 6):
                if peopleCount % 2 == 0:
                    remainder = (budget - 4200 * 0.85)
                else:
                    remainder = (budget - 4200 * 0.90)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif (peopleCount >= 7) and (peopleCount <= 11):
                if peopleCount % 2 == 0:
                    remainder = (budget - 4200 * 0.80)
                else:
                    remainder = (budget - 4200 * 0.85)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif peopleCount >= 12:
                if peopleCount % 2 == 0:
                    remainder = (budget - 4200 * 0.70)
                else:
                    remainder = (budget - 4200 * 0.75)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)

        elif season == "autumn":
            if (peopleCount >= 4) and (peopleCount <= 6):
                remainder = (budget - 4200 * 0.90)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif (peopleCount >= 7) and (peopleCount <= 11):
                remainder = (budget - 4200 * 0.85)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif peopleCount >= 12:
                remainder = (budget - 4200 * 0.75)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)

        elif season == "winter":
            if (peopleCount >= 4) and (peopleCount <= 6):
                if peopleCount % 2 == 0:
                    remainder = (budget - 2600 * 0.85)
                else:
                    remainder = (budget - 2600 * 0.90)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif (peopleCount >= 7) and (peopleCount <= 11):
                if peopleCount % 2 == 0:
                    remainder = (budget - 2600 * 0.80)
                else:
                    remainder = (budget - 2600 * 0.85)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            elif peopleCount >= 12:
                if peopleCount % 2 == 0:
                    remainder = (budget - 2600 * 0.70)
                else:
                    remainder = (budget - 2600 * 0.75)
                if remainder >= 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)

        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")
