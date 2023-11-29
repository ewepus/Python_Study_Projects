meters = int(input())
if meters < 0:
    print("invalid")
else:
    finalPrice = meters * 7.61 * 0.82
    discount = meters * 7.61 * 0.18
    finalPrice = str(finalPrice)
    discount = str(discount)
    print("The final price is: " + finalPrice + " $.")
    print("The discount is: " + discount + " $.")
