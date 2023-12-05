import sys

n = int(input())

if n > 0:
    count = 1
    maxNumber = -sys.maxsize
    while count <= n:
        inputNumber = int(input())
        if inputNumber > maxNumber:
            maxNumber = inputNumber
        count += 1
    print(maxNumber)
else:
    print("invalid")
