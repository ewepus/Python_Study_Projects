while True:
    inputNumber = int(input())
    if (-300 <= inputNumber <= 300) or (1000 <= inputNumber <= 1600):
        print("The number is: %d" % inputNumber)
        break
    else:
        print("Invalid number!")
