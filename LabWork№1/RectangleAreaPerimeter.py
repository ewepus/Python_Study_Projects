firstX = float(input())
firstY = float(input())
secondX = float(input())
secondY = float(input())

length = abs(max(secondX, firstX) - min(secondX, firstX))
width = abs(max(secondY, firstY) - min(secondY, firstY))

print("%.2f" % (2 * (length + width)))
print("%.2f" % (length * width))
