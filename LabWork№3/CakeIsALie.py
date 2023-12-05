cakeWidth = int(input())
cakeLength = int(input())
pieceCount = cakeWidth * cakeLength

if (1001 > cakeWidth > 0) and (1001 > cakeLength > 0):
    while True:
        takenPieces = input().lower()
        if takenPieces == "stop":
            print("%d pieces are left." % pieceCount)
            break
        if int(takenPieces) >= 0:
            eatenPieces = int(takenPieces)
            pieceCount = pieceCount - eatenPieces
            if pieceCount < 0:
                print("No more cake left! You need %d pieces more." % abs(pieceCount))
                break
        else:
            print("invalid")
            break
else:
    print("invalid")
