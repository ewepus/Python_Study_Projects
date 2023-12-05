import sys

n = int(input())

if n > 0:
    count = 1
    minNumber = sys.maxsize
    while count <= n:
        inputNumber = int(input())
        if inputNumber < minNumber:
            minNumber = inputNumber
        count += 1
    print(minNumber)
else:
    print("invalid")
