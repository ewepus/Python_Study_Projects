meters = float(input())

if meters < 0:
    print("invalid")
else:
    finalPrice = meters * 7.61 * 0.82
    discount = meters * 7.61 * 0.18

    print("The final price is: %.2f $." % finalPrice)
    print("The discount is: %.2f $." % discount)
