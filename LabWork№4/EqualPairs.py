import sys

pairCount = int(input())

if pairCount == 1:
    firstNum = int(input())
    secondNum = int(input())
    pairSum = firstNum + secondNum
    print("Yes, value = %.f" % pairSum)
    
elif pairCount >= 2:
    numberToRepeatTheProcess = 1
    maxDif = -sys.maxsize
    firstNum = int(input())
    secondNum = int(input())   
    pairSum = firstNum + secondNum

    while numberToRepeatTheProcess < pairCount:
        firstNum = int(input())
        secondNum = int(input())
        nextPairSum = firstNum + secondNum
        differenceBetweenPairs = abs(nextPairSum - pairSum)
        if differenceBetweenPairs > maxDif:
            maxDif = differenceBetweenPairs
            pairSum = nextPairSum
        numberToRepeatTheProcess += 1
        
    if maxDif == 0:
        print("Yes, value = %.f" % pairSum)
    else:
        print("No, maxdiff = %.f" % maxDif)
        
else:
    print("invalid")
