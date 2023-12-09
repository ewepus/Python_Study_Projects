import sys

primeSum = 0
nonPrimeSum = 0

while True:
    divisorCount = 1
    userInput = str(input().lower())

    if userInput == "stop":
        print("Sum of all prime numbers is: %.f" % primeSum)
        print("Sum of all non prime numbers is: %.f" % nonPrimeSum)
        break

    numberInput = int(userInput)
    maxNum = -sys.maxsize
    maxNum = max(maxNum, numberInput)

    if numberInput < 0:
        print("Number is invalid")
    elif numberInput == 0:
        print("Number is invalid")
    elif numberInput == 1:
        print("Number is invalid")

    else:
        for i in range(2, maxNum + 1, 1):
            if numberInput % i == 0:
                divisorCount += 1

        if divisorCount == 2:
            primeSum += numberInput
        elif divisorCount > 2:
            nonPrimeSum += numberInput
