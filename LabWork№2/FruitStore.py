fruitName = input().lower()
dayName = input().lower()
weight = float(input())

if weight > 0:
    if dayName == "monday" or dayName == "tuesday" or dayName == "wednesday" or dayName == "thursday" or dayName == "friday":
        if fruitName == "banana":
            print("%.2f" % (2.50 * weight))
        elif fruitName == "apple":
            print("%.2f" % (1.20 * weight))
        elif fruitName == "orange":
            print("%.2f" % (0.85 * weight))
        elif fruitName == "grapefruit":
            print("%.2f" % (1.45 * weight))
        elif fruitName == "kiwi":
            print("%.2f" % (2.70 * weight))
        elif fruitName == "pineapple":
            print("%.2f" % (5.50 * weight))
        elif fruitName == "grapes":
            print("%.2f" % (3.85 * weight))
        else:
            print("error")
    elif dayName == "saturday" or dayName == "sunday":
        if fruitName == "banana":
            print("%.2f" % (2.70 * weight))
        elif fruitName == "apple":
            print("%.2f" % (1.25 * weight))
        elif fruitName == "orange":
            print("%.2f" % (0.90 * weight))
        elif fruitName == "grapefruit":
            print("%.2f" % (1.60 * weight))
        elif fruitName == "kiwi":
            print("%.2f" % (3.00 * weight))
        elif fruitName == "pineapple":
            print("%.2f" % (5.60 * weight))
        elif fruitName == "grapes":
            print("%.2f" % (4.20 * weight))
        else:
            print("error")
    else:
        print("error")
else:
    print("error")
