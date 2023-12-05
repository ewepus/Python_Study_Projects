temperature = int(input())
daytime = str(input()).lower()

if (temperature >= 10) and (temperature <= 42):
    if daytime == "morning":
        if (temperature >= 10) and (temperature <= 18):
            print("It's %.f degrees, get your Sweatshirt and Sneakers" % temperature)
        elif (temperature >= 18) and (temperature <= 24):
            print("It's %.f degrees, get your Shirt and Moccasins" % temperature)
        elif temperature >= 25:
            print("It's %.f degrees, get your T-Shirt and Sandals" % temperature)

    elif daytime == "afternoon":
        if (temperature >= 10) and (temperature <= 18):
            print("It's %.f degrees, get your Shirt and Moccasins" % temperature)
        elif (temperature >= 18) and (temperature <= 24):
            print("It's %.f degrees, get your T-Shirt and Sandals" % temperature)
        elif temperature >= 25:
            print("It's %.f degrees, get your Swim Suit and Barefoot" % temperature)

    elif daytime == "evening":
        if (temperature >= 10) and (temperature <= 18):
            print("It's %.f degrees, get your Shirt and Moccasins" % temperature)
        elif (temperature >= 18) and (temperature <= 24):
            print("It's %.f degrees, get your Shirt and Moccasins" % temperature)
        elif temperature >= 25:
            print("It's %.f degrees, get your Shirt and Moccasins" % temperature)
    else:
        print("invalid")
else:
    print("invalid")
