filmType = str(input()).lower()
rowNumber = int(input())
columnNumber = int(input())

if rowNumber >= 0 and columnNumber >= 0:
    if filmType == "premiere":
        print("%.2f $" % (12 * rowNumber * columnNumber))
    elif filmType == "normal":
        print("%.2f $" % (7.5 * rowNumber * columnNumber))
    elif filmType == "discount":
        print("%.2f $" % (5 * rowNumber * columnNumber))
    else:
        print("invalid")
else:
    print("invalid")
